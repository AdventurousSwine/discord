import discord
from discord.ext import commands
import asyncio

bot=commands.Bot (command_prefix="$", case_insensitive=True)

# --------------------------------------------------------------------

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Moderation-----------------------------------------------------------------------
    prequel = bot.get_guild(778675100618588202)
    @commands.command()
    @commands.has_any_role (778715058069831730, 793993238587375626)
    async def status(self, ctx):
        """Status check"""
        # if ctx.author.id == your id
        await ctx.send("I have spoken")

    @commands.command()
    @commands.has_any_role (778715058069831730, 793993238587375626)
    async def dm(self, ctx, member: discord.User, *, words):
        """Directly message a user"""
        await member.send(words)
        await ctx.send("Sent!")
    @dm.error
    async def dm_error(ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f"Hey trooper, the error was {error} Fix it!")

    @commands.command()
    @commands.has_role (778715058069831730)
    async def warn(self, ctx, member: discord.User, *, words):
        """Warn a user"""
        await member.send(words)
        prequel = self.bot.get_guild(778675100618588202)
        channel = prequel.get_channel(812315550855987200)
        await channel.send(f"{member.mention} was warned by {ctx.author.mention} with {words}")
        await ctx.message.delete()
        await channel.send("Sent!")
    @warn.error
    async def warn_error(ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f"Hey trooper, the error was {error} Fix it!")

    @commands.command()
    @commands.has_role(778715058069831730)
    async def mute(self, ctx, member: discord.Member, words):
        """Mute a user indefinitely"""
        prequel = self.bot.get_guild(778675100618588202)
        channel = prequel.get_channel(812315550855987200)
        guild_obj = ctx.guild
        if not member:
            await ctx.send("Please specify a member")
            return
        else:
            mute_role = guild_obj.get_role(799143276862373918)
            await member.add_roles(mute_role)
            await channel.send(f"{member.mention} was muted by {ctx.author.mention} with {words} as the reason")
            await ctx.message.delete()
            await ctx.send(f"{member.mention} was muted")
    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f"Hey trooper, the error was {error} Fix it!")

    @commands.command()
    @commands.has_role(778715058069831730)
    async def tempmute(self, ctx, member: discord.Member, length: int, words):
        """Temporarily mute a user using the time in minutes"""
        prequel = self.bot.get_guild(778675100618588202)
        channel = prequel.get_channel(812315550855987200)
        guild_obj = ctx.guild
        if not member:
            await ctx.send("Please specify a member")
            return
        else:
            mute_role = guild_obj.get_role(799143276862373918)
            await member.add_roles(mute_role)
            await channel.send(f"{member.mention} was temporarily muted by {ctx.author.mention} with {words} as the reason")
            await ctx.message.delete()
            await ctx.send(f"{member.mention} was muted")
            length = length * 60
            await asyncio.sleep(length)
            await member.remove_roles(mute_role)
            await ctx.send(f"{member.mention} was unmuted")
    @tempmute.error
    async def tempmute_error(ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f"Hey trooper, the error was {error} Fix it!")

    @commands.command()
    @commands.has_role(778715058069831730)
    async def unmute(self, ctx, member: discord.Member):
        """Unmute a currently muted user"""
        guild_obj = ctx.guild
        if not member:
            await ctx.send("Please specify a member")
            return
        else:
            mute_role = guild_obj.get_role(799143276862373918)
            await member.remove_roles(mute_role)
            await ctx.message.delete()
            await ctx.send(f"{member.mention} was unmuted")
    @unmute.error
    async def unmute_error(ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f"Hey trooper, the error was {error} Fix it!")


def setup(bot):
    bot.add_cog(Moderation(bot))