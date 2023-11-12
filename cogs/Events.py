import discord
from discord.ext import commands
import json
from variable import formatter

import i18n
import os

lang = os.environ["LANGUAGE"]

def hex_to_discord_color(hex_color):
    hex_color = hex_color.lstrip('#')
    try:
        return discord.Color(int(hex_color, 16))
    except:
        return discord.Color.default()

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("config.json","r",encoding="utf-8") as f:
            config = json.load(f)

        if config['leave']['activate'] == "y":
            leave_channel = self.bot.get_channel(int(config['leave']['channel']))
        else:
            leave_channel = None
        if leave_channel:
            print(config['leave']['embed']['title'])
            title = formatter(f"{config['leave']['embed']['title']}",member,member.guild)
            description = formatter(f"{config['leave']['embed']['description']}", member, member.guild)
            author = formatter(f"{config['leave']['embed']['author']}", member, member.guild)
            author_avatar = formatter(f"{config['leave']['embed']['author_avatar']}", member, member.guild)
            thumbnail = formatter(f"{config['leave']['embed']['thumbnail']}", member, member.guild)
            footer = formatter(f"{config['leave']['embed']['footer']}", member, member.guild)
            footer_url = formatter(f"{config['leave']['embed']['footer-url']}", member, member.guild)
            img = formatter(f"{config['leave']['embed']['image']}", member, member.guild)
            color= hex_to_discord_color(config['leave']['embed']['color'])
            if config['leave']['embeds'] == "y":
                
                embed = discord.Embed()
                if title:
                    embed.title = title
                if description:
                    embed.description = description 
                if author and author_avatar:
                    embed.set_author(name=author, icon_url=author_avatar)
                if author and not author_avatar:
                    embed.set_author(name=author)
                if thumbnail:

                    embed.set_thumbnail(url=thumbnail)
                for field in config['leave']['embed']['fields']:
                    name = formatter(field['name'], member, member.guild)
                    value = formatter(field['value'], member, member.guild)
                    embed.add_field(name=name, value=value, inline=field['inline'])
                if footer and footer_url:
                    embed.set_footer(text=footer, icon_url=footer_url)
                if footer and not footer_url:
                    embed.set_footer(text=footer)
                if color:
                    embed.color = color
                if img:
                    embed.set_image(url=img)
                if config['leave']['message']:
                    message = formatter(f"{config['leave']['message']}", member, member.guild)
                    await leave_channel.send(content=message,embed=embed)
                else:
                    await leave_channel.send(embed=embed)
            else:
                if config['leave']['message']:
                    message = formatter(f"{config['leave']['message']}", member, member.guild)
                    await leave_channel.send(content=message)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{i18n.t('Events:CONNECTED_AS', locale=lang, ME=f'{self.bot.user} - ({self.bot.user.id})')}")
        if(os.environ["LIST_SERVERS"] == "True"):
            for guild in self.bot.guilds:
                print(f"{guild.name} ({guild.id})")
        with open("config.json","r") as f:
            config = json.load(f)
        if config['statut']['playing'] == "y":
            if config['statut']['text']:
                await self.bot.change_presence(activity=discord.Game(name=config['statut']['text']))
                return
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

async def setup(bot):
    await bot.add_cog(Events(bot))