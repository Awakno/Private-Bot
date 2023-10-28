import discord
from discord.ext import commands
import json
from variable import formatter
class TempoVocal(discord.Cog):
    def __init__(self,bot) -> None:
        super().__init__()
        self.bot = bot
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        s = self.bot.get_guild(member.guild.id)
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        if config['tempo-vocal']['activate'] == "y":
            if before.channel != after.channel:
                if after.channel:
                    if after.channel.id == config['tempo-vocal']['hub']:
                        names = formatter(config['tempo-vocal']['names'], member)
                        category = s.get_channel(config['tempo-vocal']['categories'])
                        new_channel = await s.create_voice_channel(names,category=category)
                        await member.move_to(new_channel)
                    if before.channel:
                        if before.channel.name in formatter(config['tempo-vocal']['names'], member):
                            await before.channel.delete()
                if not after.channel:
                    print("hello")
                    namess = formatter(config['tempo-vocal']['names'], member)
                    if before.channel.name in namess:
                        
                        await before.channel.delete()
                



def setup(bot):
    bot.add_cog(TempoVocal(bot))