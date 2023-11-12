import discord
from discord.ext import commands
import i18n
import os

lang = os.environ["LANGUAGE"]

class Moderation(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="kick", description=i18n.t("Moderation:KB_DESCRIPTION", locale=lang, KOB="kicking"))
    async def kick(self, ctx, member: discord.Member=None, *, reason="No reason provided"):
        prefix = self.bot.command_prefix
        if not ctx.author.guild_permissions.kick_members:
            return await ctx.send(i18n.t("Moderation:KB_MISSING_PERMISSION", locale=lang, KOB="kick"))
        if not member:
            return await ctx.reply(i18n.t("Moderation:KB_SYNTAX", locale=lang, PREFIX=prefix, KOB="kick"))
        try:
            await member.send(i18n.t("Moderation:KB_SUCCESS_MESSAGE", locale=lang, KOB="kicked", GUILD=ctx.guild.name, REASON=reason, AUTHOR=ctx.author))
        except:
            pass
        try:
            await member.kick(reason=reason)
        except:
            return await ctx.reply(i18n.t("Moderation:SELF_MISSING_PERMISSION", locale=lang, KOB="kick"))
        await ctx.send(i18n.t("Moderation:KB_SUCCESS", locale=lang, MEMBER=member, KOB="kicked"))

    @commands.command(name="ban", description=i18n.t("Moderation:KB_DESCRIPTION", locale=lang, KOB="banning"))
    async def ban(self, ctx, member: discord.Member=None, *, reason="No reason provided"):
        prefix = self.bot.command_prefix
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send(i18n.t("Moderation:KB_MISSING_PERMISSION", locale=lang, KOB="ban"))
        if not member:
            return await ctx.reply(i18n.t("Moderation:KB_SYNTAX", locale=lang, PREFIX=prefix, KOB="ban"))
        try:
            await member.send(i18n.t("Moderation:KB_SUCCESS_MESSAGE", locale=lang, KOB="banned", GUILD=ctx.guild.name, REASON=reason, AUTHOR=ctx.author))
        except:
            pass
        try:
            await member.ban(reason=reason)
        except:
            return await ctx.reply(i18n.t("Moderation:SELF_MISSING_PERMISSION", locale=lang, KOB="ban"))
        await ctx.send(i18n.t("Moderation:KB_SUCCESS", locale=lang, MEMBER=member, KOB="banned"))

async def setup(bot):
    await bot.add_cog(Moderation(bot))