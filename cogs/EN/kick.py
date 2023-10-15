import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="kick", description="Allows kicking a member")
    async def kick(self, ctx, member: discord.Member=None, *, reason="No reason provided"):
        if not ctx.author.guild_permissions.kick_members:
            return await ctx.send("You do not have permission to kick a member")
        if not member:
            return await ctx.reply("Syntax: `$kick <member> [<reason>]`")
        try:
            await member.kick(reason=reason)
        except:
            return await ctx.reply("I do not have permission to kick this member")
        await ctx.send(f"{member} has been successfully kicked")
        try:
            await member.send(f"You have been kicked from {ctx.guild.name} for {reason} by {ctx.author}")
        except:
            pass

def setup(bot):
    bot.add_cog(Kick(bot))
