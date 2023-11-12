from discord.ext import commands
import discord
import i18n
import os

lang = os.environ["LANGUAGE"]

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(embed=discord.Embed(title=i18n.t("Avatars:USER", locale=lang, MEMBER_NAME=member.name)).set_image(url=member.display_avatar.url))

    @commands.command(name="servericon")
    async def servericon(self, ctx):
        if(ctx.guild.icon != None):
            await ctx.send(embed=discord.Embed(title=i18n.t("Avatars:SERVER", locale=lang)).set_image(url=ctx.guild.icon.url))
        else:
            await ctx.send(embed=discord.Embed(title=i18n.t("Avatars:SERVER_NO_ICON", locale=lang)))

async def setup(bot):
    await bot.add_cog(Avatar(bot))