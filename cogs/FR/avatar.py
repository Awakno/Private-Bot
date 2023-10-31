from discord.ext import commands
import discord

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="avatar")
    async def avatar(self,ctx,member:discord.Member=None):
        if member is None:
            member = ctx.author
        await ctx.send(embed = discord.Embed(title=f"🖼️ Avatar de {member.name}").set_image(url=member.display_avatar.url))
    @commands.command(name="servericon")
    async def servericon(self,ctx):
        
        await ctx.send(embed = discord.Embed(title=f"🖼️ Icon du serveur").set_image(url=ctx.guild.icon.url))


def setup(bot):
    bot.add_cog(Avatar(bot))