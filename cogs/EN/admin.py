import discord
from discord.ext import commands
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    @commands.command(name="setprefix")
    async def set_prefix(self, ctx, prefix):
        with open("config.json", "r") as f:
            config = json.load(f)
        
        if ctx.author.id in config['owner']:
            config['prefix'] = prefix  # Modifier la valeur de la clé 'prefix'
            self.bot.command_prefix = prefix

            # Enregistrer les changements dans le fichier JSON
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)

            await ctx.send(f"Préfix changed ! new prefix is : `{prefix}`")
        else:
            await ctx.send("You are not owner of bot", delete_after=3)
    
def setup(bot):
    bot.add_cog(Admin(bot))
