import discord
import random
import asyncio

from discord.ext import commands


class gonk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels = [279753800112144385, 703785658291978330, 482260639562334228]  # put IDs here
        self.words = ["Gonk"] # put others here if you want different versions
        self.minute_bounds = (1*60, 432000) # 10s to 60s, change this (1m - 1h)
        self.loop = bot.loop.create_task(self.random_gonk())
        self.stop = False

    async def random_gonk(self):
        await asyncio.sleep(5)
        while not self.stop:
            try:
                channel = self.bot.get_channel(random.choice(self.channels))
                await channel.send(random.choice(self.words))
            except:
                pass
            await asyncio.sleep(random.randint(self.minute_bounds[0], self.minute_bounds[1]))

    @commands.command()
    @commands.has_role(279755085943144460)
    async def stop_gonk(self, ctx):
        self.stop = True

def setup(bot):
    bot.add_cog(gonk(bot))