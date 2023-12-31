import discord
from discord.ext import commands
from datetime import datetime
import json

class LogsEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        f = open("config.json", "r")
        config = json.load(f)
        self.log_channel_id = int(config['logs']['channel'])   # Replace this with the log channel ID

    @commands.Cog.listener()
    async def on_ready(self):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Bot online", value=f">>> Connected as: {self.bot.user} ({self.bot.user.id})")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore messages from bots

        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message received", value=f">>> Author: {message.author.mention}\nContent: {message.content}\nChannel: {message.channel.mention}")
            embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
            embed.set_footer(text=f"Author ID: {message.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Member joined", value=f">>> {member.mention}\nServer: {member.guild.name}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"Member ID: {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Member left", value=f">>> {member.mention}\nServer: {member.guild.name}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"Member ID: {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            if before.nick != after.nick:
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name="Nickname changed", value=f">>> {after.mention}\nNew nickname: {after.nick}")
                embed.set_author(name=f"{after}", icon_url=after.display_avatar.url)
                embed.set_footer(text=f"Member ID: {after.id}")
                await log_channel.send(embed=embed)
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)
            if added_roles or removed_roles:
                added_roles_text = " ".join([f"{role.mention}" for role in added_roles])
                removed_roles_text = " ".join([f"{role.mention}" for role in removed_roles])
                embed = discord.Embed(timestamp=datetime.now())
                if added_roles:
                    embed.add_field(name="Roles added", value=f">>> {added_roles_text}")
                if removed_roles:
                    embed.add_field(name="Roles removed", value=f">>> {removed_roles_text}")
                # Get the member who modified the roles
                async for entry in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
                    mod_member = entry.user
                embed.add_field(name="Modified by", value=f"{mod_member.mention}")
                embed.set_author(name=f"{after}", icon_url=after.display_avatar.url)
                embed.set_footer(text=f"Member ID: {after.id}")
                await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel and before.content != after.content:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message edited", value=f">>> Author: {after.author.mention}\nOld message: {before.content}\nNew message: {after.content}")
            embed.set_author(name=f"{after.author}", icon_url=after.author.display_avatar.url)
            embed.set_footer(text=f"Author ID: {after.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Role created", value=f">>> Name: {role.name}\nID: {role.id}\nColor: {role.color}")
            # Get the author of the role creation from the audit log
            async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
                author = entry.user
            embed.add_field(name="Created by", value=f"> {author.mention}")
            try:
                embed.set_author(name="Role created", icon_url=role.guild.icon.url)
            except:
                embed.set_author(name="Role created")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Role deleted", value=f">>> Name: {role.name}\nID: {role.id}")
            # Get the author of the role deletion from the audit log
            async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
                author = entry.user
            embed.add_field(name="Deleted by", value=f"> {author.mention}")
            try:
                embed.set_author(name="Role deleted", icon_url=role.guild.icon.url)
            except:
                embed.set_author(name="Role deleted")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(channel, discord.TextChannel):
                channel_type = "Text Channel"
            elif isinstance(channel, discord.VoiceChannel):
                channel_type = "Voice Channel"
            elif isinstance(channel, discord.CategoryChannel):
                channel_type = "Category"
            elif isinstance(channel, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Unknown"
            embed.add_field(name=f"Channel created ({channel_type})", value=f"Name: {channel.name}\nID: {channel.id}")
            async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
                author = entry.user
            embed.add_field(name="Created by", value=f"> {author.mention}")
            embed.set_author(name=f"Channel created ({channel_type})", icon_url=channel.guild.icon.url)
            embed.set_footer(text=f"Server ID: {channel.guild.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(after, discord.TextChannel):
                channel_type = "Text Channel"
            elif isinstance(after, discord.VoiceChannel):
                channel_type = "Voice Channel"
            elif isinstance(after, discord.CategoryChannel):
                channel_type = "Category"
            elif isinstance(after, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Unknown"
            
            embed.add_field(name=f"Channel Updated ({channel_type})", value=f"Name: {before.name} (ID: {before.id})")
            embed.add_field(name="Changes", value=f"Updated: {after.name} (ID: {after.id})")
            async for entry in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update):
                author = entry.user
            embed.add_field(name="Updated by", value=f"> {author.mention}")
            embed.set_author(name=f"Channel Updated ({channel_type})", icon_url=after.guild.icon.url)
            embed.set_footer(text=f"Server ID: {after.guild.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_kick(self, guild, member):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            action_type = "Kick"
            reason = "No reason provided"
            embed.add_field(name=f"{action_type} of a member", value=f"> User: {member.mention}\nServer: {guild.name}")
            embed.add_field(name="Reason", value=reason)
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if entry.target == member:
                    author = entry.user
            embed.add_field(name=f"By {action_type}", value=f"{author.mention}")
            embed.set_author(name=f"{member}", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"Member ID: {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message deleted", value=f"> Message: {message.content}")
            embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
            embed.set_footer(text=f"Author ID: {message.author.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Member banned", value=f"> User: {user.mention}\nServer: {guild.name}")
            embed.add_field(name="Reason", value=user.ban_reason if isinstance(user, discord.Member) else "No reason provided")
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if entry.target == user:
                    author = entry.user
            embed.add_field(name="By Banning", value=f"> {author.mention}")
            embed.set_author(name=f"{user}", icon_url=user.display_avatar.url)
            embed.set_footer(text=f"Member ID: {user.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            embed.add_field(name="Message deleted", value=f"> Message: {message.content}")
            embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
            embed.set_footer(text=f"Author ID: {message.author.id}")
            await log_channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(timestamp=datetime.now())
            if isinstance(channel, discord.TextChannel):
                channel_type = "Text Channel"
            elif isinstance(channel, discord.VoiceChannel):
                channel_type = "Voice Channel"
            elif isinstance(channel, discord.CategoryChannel):
                channel_type = "Category"
            elif isinstance(channel, discord.Thread):
                channel_type = "Thread"
            else:
                channel_type = "Unknown"
            embed.add_field(name=f"Channel deleted ({channel_type})", value=f"Name: {channel.name}\nID: {channel.id}")
            async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
                author = entry.user
            embed.add_field(name="Deleted by", value=f"> {author.mention}")
            embed.set_author(name=f"Channel deleted ({channel_type})", icon_url=channel.guild.icon.url)
            embed.set_footer(text=f"Server ID: {channel.guild.id}")
            await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LogsEvent(bot))