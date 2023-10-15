import discord
from discord.ext import commands

class Ban(discord.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="ban", description="Allows banning a member")
    async def ban(self, ctx, member: discord.Member=None, *, reason="No reason provided"):
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send("You do not have permission to ban a member")
        if not member:
            return await ctx.reply("Syntax: `$ban <member> [<reason>]`")
        try:
            await member.ban(reason=reason)
        except:
            return await ctx.reply("I do not have permission to ban this member")
        await ctx.send(f"{member} has been successfully banned")
        try:
            await member.send(f"You have been banned from {ctx.guild.name} for {reason} by {ctx.author}")
        except:
            pass

def setup(bot):
    bot.add_cog(Ban(bot))
