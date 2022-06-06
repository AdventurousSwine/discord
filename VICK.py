#IMPORTS------------------------------------------------------------------------
import discord
from discord.ext import commands
import random
import datetime
import asyncio
import traceback

#BOT BASICS-----------------------------------------------------------------------
bot=commands.Bot (command_prefix="$", case_insensitive=True, intents=discord.Intents.all())
bot.reply = {}
bot.variable = 0

def generate():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alias = None
    while not alias:
        alias = "".join(random.choices(alphabet, k=3))
        if alias in bot.reply.values():
            alias = None
    return alias


#EVENTS--------------------------------------------------------------------------

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("--------------")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="all of you dudes"))
    bot.load_extension("cogs.bgnitro")

@bot.event
async def on_message(message):

    blood = bot.get_guild(624052662156918805)
    if not message.guild:
        channel = blood.get_channel(782787938982690816)
        if message.content.startswith("Report:"):
            if message.author in blood.members:
                embed = discord.Embed(title=f"New report from {message.author} -  {message.author.id}", description=message.content[7:], color=discord.Color.dark_magenta(), timestamp=message.created_at)
                await channel.send("\n".join([f"<{attachment.url}>" for attachment in message.attachments]), embed=embed)
                return

    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.guild is None:
        channel = bot.get_channel(782787938982690816)
        if message.author.id in bot.reply.keys():
            fat_fucking_delete = False
            user_alias=bot.reply[message.author.id]
        else:
            fat_fucking_delete = True
            user_alias = generate()
            bot.reply[message.author.id] = user_alias
        for guild in bot.guilds:
            if message.author in guild.members:
                server = guild.name
                break
        embed = discord.Embed(title=server, description=message.content, timestamp=message.created_at, color=discord.Color.dark_magenta())
        embed.set_author(name=f"{message.author} : {message.author.id}")  # author.id/mention
        embed.add_field(name=str(datetime.datetime.now().strftime("%B %d, %Y")), value="<:Wink:709273153012236320>")
        embed = embed.set_footer(text=f"Message back with $reply {user_alias}")
        embed.set_thumbnail(url=message.author.avatar_url)
        await channel.send("\n".join([f"<{attachment.url}>" for attachment in message.attachments]), embed=embed)
        if fat_fucking_delete:
            await asyncio.sleep(172800)
            del bot.reply[message.author.id]

datetime.datetime.now().strftime("%B %d, %Y. %I:%M %p EST")

#COMMANDS-----------------------------------------------------------------------

@bot.command()
@commands.has_any_role(624451538609504256)
async def reply(ctx, alias, *, words):
    """Reply to a message sent to me"""
    for user_id, user_alias in bot.reply.items():
        if alias == user_alias:
            user = bot.get_user(user_id)
            await user.send(words)
            await ctx.send(f"Sent to {user.mention}.")
            return
    if alias.isdigit():
        user = bot.get_user(int(alias))
        if user:
            await user.send(words)
            await ctx.send(f"Sent to {user.mention}.")
            return
    await ctx.send(f"Could not find a user matching `{alias}`.")
@reply.error
async def reply_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send(f"Hey dumbass, the error was {error} Fix it!")

@bot.command()
@commands.has_any_role(624451538609504256)
async def status(ctx):
    """Status check"""
    await ctx.send("What's going on dude?")
@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send(f"Hey dumbass, the error was {error} Fix it!")

@bot.command()
@commands.has_role(624451538609504256)
async def dm(ctx, member: discord.User, *, words):
    """Directly message a user"""
    await member.send(words)
    await ctx.send("Sent!")
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send(f"Hey dumbass, the error was {error} Fix it!")

#@bot.command()
#async def swine(ctx):
#    """Swine"""
#    await ctx.send("https://tenor.com/view/fuck-not-swine-walking-back-gif-11560149")

bot.run(Token)
