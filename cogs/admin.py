import discord
from discord.ext import commands
import json
import i18n
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    @commands.command(name="setprefix")
    async def set_prefix(self, ctx, prefix):
        #Sera implémenté avec une fichier de base de donnée local
        await ctx.send("Not implemented yet", delete_after=3)
        # with open("config.json", "r") as f:
        #     config = json.load(f)
        
        # if ctx.author.id in config['owner']:
        #     config['prefix'] = prefix  # Modifier la valeur de la clé 'prefix'
        #     self.bot.command_prefix = prefix

        #     # Enregistrer les changements dans le fichier JSON
        #     with open("config.json", "w") as f:
        #         json.dump(config, f, indent=4)

        #     await ctx.send(f"Prefix updated ! New prefix: `{prefix}`")
        # else:
        #     await ctx.send("You're not one of the bot owners", delete_after=3)
    
async def setup(bot):
    await bot.add_cog(Admin(bot))