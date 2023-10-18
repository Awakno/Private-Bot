import discord
from discord.ext import commands
from datetime import datetime
import json

class LogEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        f = open("config.json", "r")
        config = json.load(f)
        if config['logs']['activate'] == "y":
            self.log_channel_id = int(config['logs']['channel'])   # Remplacez ceci par l'ID du canal de logs
        else:
            self.log_channel_id = None
    @commands.Cog.listener()
    async def on_ready(self):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Le bot est en ligne", value=f">>> Connecté en tant que : {self.bot.user} ({self.bot.user.id})")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignorer les messages des bots

        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message reçu", value=f">>> Auteur: {message.author.mention}\nContenu: {message.content}\nCanal: {message.channel.mention}")
            embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
            embed.set_footer(text=f"ID de l'auteur : {message.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Membre a rejoint", value=f">>> {member.mention}\nServeur: {member.guild.name}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Membre a quitté", value=f">>> {member.mention}\nServeur: {member.guild.name}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            if before.nick != after.nick:
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name="Changement de surnom", value=f">>> {after.mention}\nNouveau surnom: {after.nick}")
                embed.set_author(name=f"{after}", icon_url=after.display_avatar.url)
                embed.set_footer(text=f"ID du membre : {after.id}")
                await log_channel.send(embed=embed)
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)
            if added_roles or removed_roles:
                added_roles_text = " ".join([f"{role.mention}" for role in added_roles])
                removed_roles_text = " ".join([f"{role.mention}" for role in removed_roles])
                embed = discord.Embed(timestamp=datetime.now())
                if added_roles:
                    embed.add_field(name="Rôles ajoutés", value=f">>> {added_roles_text}")
                if removed_roles:
                    embed.add_field(name="Rôles supprimés", value=f">>> {removed_roles_text}")
                # Obtenir le membre qui a modifié les rôles
                async for entry in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
                    mod_member = entry.user
                embed.add_field(name="Modifié par", value=f"{mod_member.mention}")
                embed.set_author(name=f"{after}", icon_url=after.display_avatar.url)
                embed.set_footer(text=f"ID du membre : {after.id}")
                await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel and before.content != after.content:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message modifié", value=f">>> Auteur: {after.author.mention}\nAncien message: {before.content}\nNouveau message: {after.content}")
            embed.set_author(name=f"{after.author}", icon_url=after.author.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {after.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Rôle créé", value=f">>> Nom: {role.name}\nID: {role.id}\nCouleur: {role.color}")
            # Obtenir l'auteur de la création du rôle depuis le journal d'audit
            async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
                author = entry.user
            embed.add_field(name="Créé par", value=f"> {author.mention}")
            try:
                embed.set_author(name="Rôle créé", icon_url=role.guild.icon.url)
            except:
                embed.set_author(name="Rôle créé")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Rôle supprimé", value=f">>> Nom: {role.name}\nID: {role.id}")
            # Obtenir l'auteur de la suppression du rôle depuis le journal d'audit
            async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
                author = entry.user
            embed.add_field(name="Supprimé par", value=f"> {author.mention}")
            try:
                embed.set_author(name="Rôle supprimé", icon_url=role.guild.icon.url)
            except:
                embed.set_author(name="Rôle supprimé")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(channel, discord.TextChannel):
                channel_type = "Salon texte"
            elif isinstance(channel, discord.VoiceChannel):
                channel_type = "Salon vocal"
            elif isinstance(channel, discord.CategoryChannel):
                channel_type = "Catégorie"
            elif isinstance(channel, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Inconnu"
            embed.add_field(name=f"Création de salon ({channel_type})", value=f"Nom: {channel.name}\nID: {channel.id}")
            async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
                author = entry.user
            embed.add_field(name="Créé par", value=f"> {author.mention}")
            embed.set_author(name=f"Création de salon ({channel_type})", icon_url=channel.guild.icon.url)
            embed.set_footer(text=f"ID du serveur : {channel.guild.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(after, discord.TextChannel):
                channel_type = "Salon texte"
            elif isinstance(after, discord.VoiceChannel):
                channel_type = "Salon vocal"
            elif isinstance(after, discord.CategoryChannel):
                channel_type = "Catégorie"
            elif isinstance(after, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Inconnu"
            
            embed.add_field(name=f"Salon mis à jour ({channel_type})", value=f"Nom: {before.name} (ID: {before.id})")
            embed.add_field(name="Changements", value=f"Modifié en : {after.name} (ID: {after.id})")
            async for entry in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update):
                author = entry.user
            embed.add_field(name="Modifié par", value=f"> {author.mention}")
            embed.set_author(name=f"Salon mis à jour ({channel_type})", icon_url=after.guild.icon.url)
            embed.set_footer(text=f"ID du serveur : {after.guild.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_kick(self, guild, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            action_type = "Expulsion"
            reason = "Aucune raison fournie"
            embed.add_field(name=f"{action_type} d'un membre", value=f"> Membre : {member.mention}\nServeur: {guild.name}")
            embed.add_field(name="Raison", value=reason)
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if entry.target == member:
                    author = entry.user
            embed.add_field(name=f"Par {action_type}", value=f"{author.mention}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message supprimé", value=f"> Message : {message.content}")
            embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {message.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Membre banni", value=f"> Membre : {user.mention}\nServeur : {guild.name}")
            embed.add_field(name="Raison", value=user.ban_reason if isinstance(user, discord.Member) else "Aucune raison fournie")
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if entry.target == user:
                    author = entry.user
            embed.add_field(name="En bannissant", value=f"> {author.mention}")
            embed.set_author(name=f"{user}", icon_url=user.display_avatar.url)
            embed.set_footer(text=f"ID du membre : {user.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(channel, discord.TextChannel):
                channel_type = "Salon texte"
            elif isinstance(channel, discord.VoiceChannel):
                channel_type = "Salon vocal"
            elif isinstance(channel, discord.CategoryChannel):
                channel_type = "Catégorie"
            elif isinstance(channel, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Inconnu"
            embed.add_field(name=f"Salon supprimé ({channel_type})", value=f"Nom: {channel.name}\nID: {channel.id}")
            async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
                author = entry.user
            embed.add_field(name="Supprimé par", value=f"> {author.mention}")
            embed.set_author(name=f"Salon supprimé ({channel_type})", icon_url=channel.guild.icon.url)
            embed.set_footer(text=f"ID du serveur : {channel.guild.id}")
            await log_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(LogEvents(bot))
