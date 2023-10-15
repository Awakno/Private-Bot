import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="userinfo", description="Displays user information")
    async def userinfo(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        message_roles = ""
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info | {member}")
        for role in roles:
            if len(message_roles) + len(role.mention) > 1020:
                message_roles += "..."
            else:
                message_roles += f"{role.mention}"
        embed.add_field(name=f"Roles[{len(roles)}]", value=message_roles, inline=False)
        embed.add_field(name="Joined", value=f"<t:{int(member.joined_at.timestamp())}> (<t:{int(member.joined_at.timestamp())}:R>)", inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Account created", value=f"<t:{int(member.created_at.timestamp())}> (<t:{int(member.created_at.timestamp())}:R>)", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo", description="Displays server information")
    async def serverinfo(self, ctx):
        embed = discord.Embed(timestamp=ctx.message.created_at)
        try:
            embed.set_author(name=f"Server Info | {ctx.guild}", icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url=ctx.guild.icon.url)
        except:
            embed.set_author(name=f"Server Info | {ctx.guild}")
        embed.add_field(name="Name", value=f"> {ctx.guild.name}", inline=False)
        embed.add_field(name="Owner", value=f"> {ctx.guild.owner.mention}", inline=False)
        embed.add_field(name="ID", value=f"> {ctx.guild.id}", inline=False)
        bot_count = sum(1 for member in ctx.guild.members if member.bot)
        embed.add_field(name="Statistics", value=f">>> :busts_in_silhouette: {ctx.guild.member_count} members \n :robot: {bot_count} bots", inline=False)
        embed.add_field(name="Channels", value=f">>> :hash: {len(ctx.guild.text_channels)} text channels\n :loud_sound: {len(ctx.guild.voice_channels)} voice channels\n :video_game: {len(ctx.guild.categories)} categories", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))
