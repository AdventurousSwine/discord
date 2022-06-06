# notes:
#

from discord.ext import commands


# --------------------------------------------------------------------

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # you do this so bot is accessible to the rest of the file

    # MATH-----------------------------------------------------------------------

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        """Add some bitches up"""
        await ctx.send(f"{a}+{b}={a + b}")

    @commands.command()
    async def subtract(self, ctx, a: int, b: int):
        """Delete some motherfuckers"""
        await ctx.send(f"{a}-{b}={a - b}")

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        """Spread your seed"""
        await ctx.send(f"{a}x{b}={a * b}")

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        """Split up some hoes"""
        await ctx.send(f"{a}/{b}={a / b}")

    @commands.command()
    async def power(self, ctx, a: int, b: int):
        """Flex on them"""
        await ctx.send(f"{a}^{b}={a ** b}")


# --------------------------------------------------------------------

def setup(bot):
    # in order to add the cog, the bot imports the file then runs setup
    # so you kinda just need to have this
    bot.add_cog(Math(bot))