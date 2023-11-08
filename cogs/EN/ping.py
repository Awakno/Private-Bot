import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "ping")
    async def ping(self,ctx):
        await ctx.send(f":ping_pong: **Pong!** {round(self.bot.latency * 1000)} ms")
    


async def setup(bot):
    await bot.add_cog(Ping(bot))