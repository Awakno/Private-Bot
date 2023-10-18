import discord
from discord.ext import commands
import json


class OnReady(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Connected as: {self.bot.user}({self.bot.user.id})")
        print("I'm on servers:")
        for guild in self.bot.guilds:
            print(f"{guild.name} ({guild.id})")
        with open("config.json","r") as f:
            config = json.load(f)
        """if config['statut']['playing'] == "y":
            if config['statut']['text']:
                await self.bot.change_presence(activity=discord.Game(name=config['statut']['text']))
                return"""
        if config['statut']['watching'] == "y":
            if config['statut']['text']:
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config['statut']['text']))
                return
        if config['statut']['listening'] == "y":
            if config['statut']['text']:
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config['statut']['text']))

                return
        if config['statut']['streaming'] == "y":
            if config['statut']['url']:
                if config['statut']['text']:
                    await self.bot.change_presence(activity=discord.Streaming(name=config['statut']['text'], url=config['statut']['url']))
                    return
        print("Ready to help !")


def setup(bot):
    bot.add_cog(OnReady(bot))
            