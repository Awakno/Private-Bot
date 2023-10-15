import discord
from discord.ext import commands
class kick(discord.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    @commands.command(name="kick",description="Permet de bannir un membre")
    async def kick(self, ctx, member: discord.Member=None, *, reason="Aucune raison fournie"):
        if not ctx.author.guild_permissions.kick_members:
            return await ctx.send("Vous n'avez pas la permission d'expulser un membre")
        if not member:
            return await ctx.reply("Synthaxe: `$kick <membre> [<raison>]`")
        try:
            await member.kick(reason=reason)
        except:
            return await ctx.reply("Je n'ai pas la permission d'expulser ce membre")
        await ctx.send(f"{member} a bien été banni")
        try:
            await member.send(f"Tu as été expulser de {ctx.guild.name} pour {reason} par {ctx.author}")
        except:
            pass

def setup(bot):
    bot.add_cog(kick(bot))