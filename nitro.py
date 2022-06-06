import random

from discord.ext import commands

class Boosting(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        #self.past_booster = self.bot.get_guild(778675100618588202).get_role(Settings.instance.RETIRED_IJLSA_MEMBER_ROLE)
        self.booster = self.bot.get_guild(778675100618588202).get_role(812394606242299916)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if self.booster not in before.roles and self.booster in after.roles:
            # We got a booster!
            await self.bot.get_channel(815015745502445598).send(f" **<@{after.id}> just boosted us** \nWe now have **{after.guild.premium_subscription_count} boosts** and are at **level {after.guild.premium_tier}**")
            # send in announcements
            message = await self.bot.get_channel(778716914771820615).send(
                "**<@{}> just boosted our server** \nMake your master proud, apprentice.\n{}".format(after.id, random.choice([
                    'https://cdn.discordapp.com/attachments/779198331473494036/815015156790722630/star-wars-force-unleashed-darth-vader-starkiller-best-star-wars-story.png',
                    'https://cdn.discordapp.com/attachments/779198331473494036/815016455161774120/de1afcf84d7f4f5ddbbcdeac1742a5b8.png',
                    'https://cdn.discordapp.com/attachments/779198331473494036/815016494395949086/maxresdefault.png',
                    'https://cdn.discordapp.com/attachments/778675101083107380/856332346441859112/image0.jpg'
                ])))

            await message.add_reaction('<:ObiLove:780630066471239680>')
            await message.add_reaction('<a:UnlimitedPower:799102189066518539>')
            #await after.remove_roles(self.past_booster)

        elif self.booster in before.roles and self.booster not in after.roles:
            # give past booster role
            #await after.add_roles(self.past_booster)
            # We lost a booster
            await self.bot.get_channel(815015745502445598).send(
                f"🥺 **<@{after.id}>'s boost just ended** 🥺\nWe now have **{after.guild.premium_subscription_count} boosts** and are at **level {after.guild.premium_tier}**")

def setup(bot):
    bot.add_cog(Boosting(bot))