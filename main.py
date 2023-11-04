import json
import os

import discord
from discord.ext import commands


with open("config.json") as f:
    config = json.load(f)

bot = commands.Bot(
    command_prefix=config['prefix'],
    intents=discord.Intents.all()
    )
lang = upper(config['lang'])
list_lang = []

for folder in os.listdir("./cogs/"):
    list_lang.append(folder)

if lang is in list_lang:
    for file in os.listdir(f"./cogs/{lang}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{lang}.{file[:-3]}")

bot.run(config['token'])