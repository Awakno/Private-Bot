import json
import os

import traceback
import sys

import discord
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)

lang = config['lang'].upper()
list_lang = []

for folder in os.listdir("./cogs/"):
    folder = folder.upper()
    list_lang.append(folder)

class PrivateBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned_or(config['prefix']),intents=discord.Intents.all())
        self.remove_command("help")

    async def LoadCogs(self):
        if lang in list_lang:
                for file in os.listdir(f"./cogs/{lang}"):
                    if file.endswith(".py"):
                        cog = f"cogs.{lang}.{file[:-3]}"
                        try:
                            await bot.load_extension(cog)
                            if(config["debug"]):
                                print(f'Loaded {cog} !', file=sys.stdout)
                        except Exception as e:
                            print(f'Failed to load {cog}.', file=sys.stderr)
                            if(config["debug"]):
                                traceback.print_exc()

    async def setup_hook(self) -> None:
        await self.LoadCogs()

bot = PrivateBot()

bot.run(config['token'])