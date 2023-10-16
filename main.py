import discord
from discord.ext import commands
import json
import os
with open("config.json") as f:
    config = json.load(f)


bot = commands.Bot(command_prefix=config['prefix'],intents=discord.Intents.all())


    
if  'fr' == config['lang'] :
    for j in os.listdir("./cogs/FR"):
        if j.endswith(".py"):
            if not j.startswith("-"):

                bot.load_extension(f"cogs.FR.{j[:-3]}")
if config['lang'] == "en":
    for j in os.listdir("./cogs/EN"):
        if j.endswith(".py"):
            if j.startswith("-"):
                bot.load_extension(f"cogs.EN.{j[:-3]}")


########


bot.run(config['token'])
