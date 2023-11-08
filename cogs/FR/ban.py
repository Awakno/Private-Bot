import discord
from discord.ext import commands
class Ban(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    @commands.command(name="ban",description="Permet de bannir un membre")
    async def ban(self, ctx, member: discord.Member=None, *, reason="Aucune raison fournie"):
        prefix = self.bot.command_prefix
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send("Vous n'avez pas la permission de bannir un membre")
        if not member:
            return await ctx.reply(f"Synthaxe: `{prefix}ban <membre> [<raison>]`")
        try:
            await member.ban(reason=reason)
        except:
            return await ctx.reply("Je n'ai pas la permission de bannir ce membre")
        await ctx.send(f"{member} a bien été banni")
        try:
            await member.send(f"Tu as été banni de {ctx.guild.name} pour {reason} par {ctx.author}")
        except:
            pass

async def setup(bot):
    await bot.add_cog(Ban(bot))