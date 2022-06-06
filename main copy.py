# notes:
# compatible with version 1.8

import discord
from discord.ext import commands

# --------------------------------------------------------------------


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, extension_name: str):
        """Loads an extension"""
        try:
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            self.bot.logger.info("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send("{} loaded.".format(extension_name))
        self.bot.logger.info("{} loaded.".format(extension_name))

    @commands.command()
    async def unload(self, ctx, extension_name: str):
        """Unloads an extension"""
        if extension_name == "startup_all.CogCommands":
            self.bot.logger.info("attempt to unload CogCommands was blocked")
            await ctx.send("You can't unload CogCommands!")
        else:
            self.bot.unload_extension(extension_name)
            await ctx.send("{} unloaded.".format(extension_name))
            self.bot.logger.info("{} unloaded.".format(extension_name))

# --------------------------------------------------------------------


def setup(bot):
    bot.add_cog(Cog(bot))
