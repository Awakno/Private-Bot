import json
import os
import sys
import traceback

from dotenv import load_dotenv

import discord
from discord.ext import commands
import i18n

load_dotenv()

i18n.load_path.append("locales")
i18n.set("file_format", "json")
i18n.set("filename_format", "{namespace}.{format}")
i18n.set("namespace_delimiter", ":")
i18n.set("skip_locale_root_data", True)
i18n.set("use_locale_dirs", True)

DEBUG = os.environ["DEBUG"] == "True"

class PrivateBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned_or(os.environ['PREFIX']),intents=discord.Intents.all())
        self.remove_command("help")

    async def LoadCogs(self):
        for file in os.listdir(f"./cogs"):
            if file.endswith(".py"):
                cog = f"cogs.{file[:-3]}"
                try:
                    await bot.load_extension(cog)
                    if(DEBUG):
                        print(f'Loaded {cog} !', file=sys.stdout)
                except Exception as e:
                    print(f'Failed to load {cog}.', file=sys.stderr)
                    if(DEBUG):
                        traceback.print_exc()

    async def setup_hook(self) -> None:
        await self.LoadCogs()

bot = PrivateBot()
bot.run(os.environ['TOKEN'])