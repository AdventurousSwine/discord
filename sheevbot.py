#IMPORTS------------------------------------------------------------------------
import discord
from discord.ext import commands
import random
import datetime
import asyncio
import traceback

#BOT BASICS-----------------------------------------------------------------------
bot=commands.Bot (command_prefix="-", case_insensitive=True)
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
async def on_ready ():
    print("Logged in as")
    print(bot.user.name)
    print("--------------")
def function_name(input_variable):
    function_name("string")
    print (input_variable)

@bot.event
async def on_message(message):

    sheev = bot.get_guild(429365222461931522)
    if not message.guild:
        channel = sheev.get_channel(731394452043726899)
        if message.content.startswith("Report:"):
            if message.author in sheev.members:
                embed = discord.Embed(title=f"New report from {message.author} -  {message.author.id}", description=message.content[7:], color=discord.Color.dark_magenta(), timestamp=message.created_at)
                await channel.send("\n".join([f"<{attachment.url}>" for attachment in message.attachments]), embed=embed)
                return

    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.guild is None:
        channel = bot.get_channel(731394452043726899)
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
        embed.add_field(name=str(datetime.datetime.now().strftime("%B %d, %Y")), value="<:blank:731000061571366972>")
        embed = embed.set_footer(text=f"Message back with -reply {user_alias}")
        embed.set_thumbnail(url=message.author.avatar_url)
        await channel.send("\n".join([f"<{attachment.url}>" for attachment in message.attachments]), embed=embed)
        if fat_fucking_delete:
            await asyncio.sleep(86400)
            del bot.reply[message.author.id]

datetime.datetime.now().strftime("%B %d, %Y. %I:%M %p EST")

#COMMANDS-----------------------------------------------------------------------

@bot.command()
@commands.has_any_role(429365696938377228)
async def reply(ctx, alias, *, words):
    """Reply to a message sent to me"""
    for user_id, user_alias in bot.reply.items():
        if alias == user_alias:
            user = bot.get_user(user_id)
            await user.send(words)
            await ctx.send(f"Sent to {user.mention}.")
            return
@reply.error
async def reply_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send(f"The error was {error}")
        '\n'.join(traceback.format_exception(type(exception), exception, exception.__traceback__))

@bot.command()
@commands.has_any_role(429365696938377228)
async def status(ctx):
    """Status check"""
    await ctx.send("Yuh Yeet")
@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send(f"The error was {error}")

@bot.command()
async def swine(ctx):
    """Swine"""
    await ctx.send("https://tenor.com/view/fuck-not-swine-walking-back-gif-11560149")

bot.run(Token)
