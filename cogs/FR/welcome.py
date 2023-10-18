import discord
from discord.ext import commands
import json
from variable import formatter

def hex_to_discord_color(hex_color):
    hex_color = hex_color.lstrip('#')
    try:
        return discord.Color(int(hex_color, 16))
    except:
        return discord.Color.default()

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("config.json","r",encoding="utf-8") as f:
            config = json.load(f)
        if config['welcome']['activate'] == "y":
            welcome_channel = self.bot.get_channel(int(config['welcome']['channel']))
        else:
            welcome_channel = None
        if welcome_channel:
            print(config['welcome']['embed']['title'])
            title = formatter(f"{config['welcome']['embed']['title']}",member,member.guild)
            description = formatter(f"{config['welcome']['embed']['description']}", member, member.guild)
            author = formatter(f"{config['welcome']['embed']['author']}", member, member.guild)
            author_avatar = formatter(f"{config['welcome']['embed']['author_avatar']}", member, member.guild)
            thumbnail = formatter(f"{config['welcome']['embed']['thumbnail']}", member, member.guild)
            footer = formatter(f"{config['welcome']['embed']['footer']}", member, member.guild)
            footer_url = formatter(f"{config['welcome']['embed']['footer-url']}", member, member.guild)
            img = formatter(f"{config['welcome']['embed']['image']}", member, member.guild)
            color= hex_to_discord_color(config['welcome']['embed']['color'])
            if config['welcome']['embeds'] == "y":
                
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
                for field in config['welcome']['embed']['fields']:
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
                if config['welcome']['message']:
                    message = formatter(f"{config['welcome']['message']}", member, member.guild)
                    await welcome_channel.send(content=message,embed=embed)
                else:
                    await welcome_channel.send(embed=embed)
            else:
                if config['welcome']['message']:
                    message = formatter(f"{config['welcome']['message']}", member, member.guild)
                    await welcome_channel.send(content=message)

def setup(bot):
    bot.add_cog(Welcome(bot))