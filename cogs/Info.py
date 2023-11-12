import discord
from discord.ext import commands
import i18n
import os

lang = os.environ["LANGUAGE"]

class Info(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="userinfo", description=i18n.t("Info:UI_DESCRIPTION", locale=lang))
    async def userinfo(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        message_roles = ""
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=i18n.t("Info:INFO_AUTHOR", locale=lang, MEMBER_OR_SERVER="User", MEMBER_OR_SERVER2=member))
        for role in roles:
            if len(message_roles) + len(role.mention) > 1020:
                message_roles += "..."
            else:
                message_roles += f"{role.mention}"
        embed.add_field(name=f"Roles[{len(roles)}]", value=message_roles, inline=False)
        embed.add_field(name=i18n.t("Info:USER_JOINED", locale=lang), value=f"<t:{int(member.joined_at.timestamp())}> (<t:{int(member.joined_at.timestamp())}:R>)", inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name=i18n.t("Info:USER_CREATED", locale=lang), value=f"<t:{int(member.created_at.timestamp())}> (<t:{int(member.created_at.timestamp())}:R>)", inline=False)
        embed.set_footer(text=i18n.t("General:REQUESTED_BY", locale=lang, MEMBER_NAME=ctx.author), icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo", description=i18n.t("Info:SI_DESCRIPTION", locale=lang))
    async def serverinfo(self, ctx):
        embed = discord.Embed(timestamp=ctx.message.created_at)

        if(ctx.guild.icon != None):
            embed.set_author(name=i18n.t("Info:INFO_AUTHOR", locale=lang, MEMBER_OR_SERVER="Server", MEMBER_OR_SERVER2=ctx.guild), icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url=ctx.guild.icon.url)
        else:
            embed.set_author(name=i18n.t("Info:INFO_AUTHOR", locale=lang, MEMBER_OR_SERVER="Server", MEMBER_OR_SERVER2=ctx.guild))
            
        embed.add_field(name=i18n.t("General:NAME", locale=lang), value=f"> {ctx.guild.name}", inline=False)
        embed.add_field(name=i18n.t("General:OWNER", locale=lang), value=f"> {ctx.guild.owner.mention}", inline=False)
        embed.add_field(name="ID", value=f"> {ctx.guild.id}", inline=False)
        bot_count = sum(1 for member in ctx.guild.members if member.bot)
        embed.add_field(name=i18n.t("General:STATS", locale=lang), value=f">>> :busts_in_silhouette: {ctx.guild.member_count} {i18n.t('General:MEMBERS', locale=lang)} \n :robot: {bot_count} {i18n.t('General:BOTS', locale=lang)}", inline=False)
        embed.add_field(name=i18n.t("General:CHANNEL", locale=lang), value=f">>> :hash: {len(ctx.guild.text_channels)} text {i18n.t('General:CHANNEL', locale=lang)}s\n :loud_sound: {len(ctx.guild.voice_channels)} voice {i18n.t('General:CHANNEL', locale=lang)}s\n :video_game: {len(ctx.guild.categories)} categories", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))