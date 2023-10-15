import discord
from discord.ext import commands
import json
class OnReady(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Connectés en tant que: {self.bot.user}({self.bot.user.id})")
        print("Je suis sur les serveurs suivants:")
        for guild in self.bot.guilds:
            print(f"{guild.name} ({guild.id})")
        try:
            with open("presence.json", "r") as f:
                presence_data = json.load(f)
                activity_type = presence_data["activity_type"]
                activity_name = presence_data["activity_name"]
                activity = discord.Activity(name=activity_name, type=getattr(discord.ActivityType, activity_type.capitalize()))
                await self.bot.change_presence(activity=activity)
        except FileNotFoundError:
            # Handle the case when the file doesn't exist
            pass

        # Set the bot's presence on startup
        
        print("Prêt à aider !")


def setup(bot):
    bot.add_cog(OnReady(bot))
            