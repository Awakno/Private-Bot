import discord
from discord.ext import commands
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    #soon
    
def setup(bot):
    bot.add_cog(Admin(bot))
