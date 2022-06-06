#IMPORTS------------------------------------------------------------------------
import discord
from discord.ext import commands
import random
import datetime
import asyncio
import ast
import os

#BOT BASICS-----------------------------------------------------------------------
bot=commands.Bot (command_prefix="$", case_insensitive=True)
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

#reactions = {
 #   id: other_id,
  #  id: other_id
#}

points = {352216606098587650: 10}



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

    Sage = bot.get_guild(404065497827508224)
    if not message.guild:
        channel = Sage.get_channel(706936970189733948)
        if message.content.startswith("Report:"):
            if message.author in SWS.members:
                embed = discord.Embed(title=f"New report from {message.author} -  {message.author.id}",
                                      description=message.content[7:], color=discord.Color.dark_magenta(),
                                      timestamp=message.created_at)
                await channel.send("\n".join([f"<{attachment.url}>" for attachment in message.attachments]),
                                   embed=embed)
                return

    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.guild is None:
        #channel = bot.get_channel(704231953368481896) #Organa
        #channel = bot.get_channel(671122086793576498) #Juan
        channel = bot.get_channel(706936970189733948)  #Sage
        if message.author.id in bot.reply.keys():
            fat_fucking_delete = False
            # if they have a stored alias
            user_alias=bot.reply[message.author.id]
            # retrieves alias from storage instead of making a new one, stores it in a local variable again
            # send embed message, once again using user_alias
        else:
            fat_fucking_delete = True
            user_alias = generate()
            # stores in a "local" variable to keep track of and use in a minute
            #bot.variable = bot.variable + 1
            # this makes it give them the next number next time
            bot.reply[message.author.id] = user_alias
            # stores the user alias in the dict
            # send embed message, use user_alias inside f string to tell you the alias to use
            #user_alias[key] = value creates a new key value pair
            # reply

        for guild in bot.guilds:
            if message.author in guild.members:
                server = guild.name
                break
        embed = discord.Embed(title=server, description=message.content, timestamp=message.created_at, color=discord.Color.dark_magenta())
        #embed = embed.set_footer(text=f"Message back with $reply {user_alias}")
        embed.set_author(name=str(message.author)) #author.id/mention
        embed.add_field(name=str(datetime.datetime.now().strftime("%B %d, %Y")), value="<:blank:316406561876606977>")
        embed = embed.set_footer(text=f"Message back with $reply {user_alias}")
        embed.set_thumbnail(url=message.author.avatar_url) #set_image/thumbnail
        await channel.send(embed=embed)
            #channel = bot.get_channel(671840056587059206)
            #await channel.send(message.content)
            #user = bot.get_user(p298497141490450432)
            #await user.send(message.content)
        if fat_fucking_delete:
            await asyncio.sleep(600)
            del bot.reply[message.author.id]

datetime.datetime.now().strftime("%B %d, %Y. %I:%M %p EST")

#@bot.event
#async def on_raw_reaction_add(payload):
#    if payload.message_id == 704215707616935956:
#        if payload.emoji.id in reactions.keys():
#            guild = bot.get_guild(payload.guild_id)
#            member = guild.get_member(payload.user_id)
#            for role in reactions:
#                if role == payload.emoji.id:
#                    await member.add_roles(guild.get_role(reactions[role]))
#                else:
#                    await member.remove_roles(guild.get_role(reactions[role]))

#@bot.event
#async def on_raw_reaction_remove(payload):
#    if payload.message_id == 704215707616935956:
#        if payload.emoji.id in reactions.keys():
#            role_id = reactions[payload.emoji.id]
#            guild = bot.get_guild(payload.guild_id)
#            member = guild.get_member(payload.user_id)
#            role = guild.get_role(role_id)
#            await member.remove_roles(role)

#@bot.event
#async def on_reaction_add(reaction, user):
#    if reaction.message.id == 704215707616935956:
#        if reaction.emoji.id in reactions:
#            for role in reactions:
#                if role == reaction.emoji.id:
#                    await reaction.guild.get_member(user.id).add_roles(role)
#                else:
#                    await reaction.guild.get_member(user.id).remove_roles(role)
#            for m_reaction in reaction.message.reactions:
#                if m_reaction != reaction:
#                    try:
#                        await m_reaction.remove(user)
#                    except:
#                        pass
#        else:
#            await reaction.remove(user)

#COMMANDS-----------------------------------------------------------------------

@bot.command()
async def addpoint(ctx, member: discord.Member, amount: int):
    if 352216606098587650 in points:
        points[352216606098587650] = points[352216606098587650] + amount
        await ctx.send(f"{amount} points were added to {member.mention} for the {side} side")
    else:
        points[352216606098587650] = amount
        await ctx.send(f"{member.mention} is currently at {amount} points")

#@bot.command()
#async def status(ctx):
#    """Status check"""
#    # if ctx.author.id == your id
#    await ctx.send("Yuh Yeet")

#@bot.command()
#@commands.has_role (699307632825204786)
#async def sage(ctx):
#    """Sage"""
#    await ctx.send("Punk ass bitch")

#@bot.command()
#async def morning(ctx):
#    """Good Morning!"""
#    await ctx.send(f"Shut the fuck up, {ctx.author.mention}")

#@bot.command()
#async def clench(ctx):
#   """Clenching"""
#   await ctx.send("<:clench:699908479271436338>")

#bot.command()
#async def rev(ctx):
#   """this is how you make a command description"""
#   await ctx.send("Smol pp")

#@bot.command()
#async def bread(ctx):
#   """this is how you make a command description"""
#   await ctx.send("Big good")

#@bot.command()
#async def hello(ctx):
#   """Hello"""
#   await ctx.send(f"Hello, {ctx.author.mention}!")

#@bot.command()
#async def butt(ctx, *, member: discord.Member=None):
#    """Butt"""
#    if member is not None:
#        await ctx.send(f"Eat ass, {member.mention}")
#    else:
#        await ctx.send(f"Eat ass, {ctx.author.mention}")

#@bot.command()
#async def stfu(ctx, *, thing=None):
#   """stfu"""
#   if thing is not None:
#        await ctx.send(f"Shut the fuck up, {thing}")
#   else:
#        await ctx.send(f"Shut the fuck up, {ctx.author.mention}")

@bot.command()
#@commands.has_role (279755085943144460)
async def say(ctx, c: discord.TextChannel, *, words):
    """Send a message to a channel"""
    await c.send(words)

#@bot.command()
#@commands.has_role (279755085943144460)
#async def dm(ctx, member: discord.User, *, words):
#    """Directly message a user"""
#    await member.send(words)
#    await ctx.send("Sent!")

#@bot.command()
#@commands.has_role (279755085943144460)
#async def warn(ctx, member: discord.User, *, words):
#    """Warn a user"""
#    await member.send(words)
#    SWS = bot.get_guild(459158948801544192)
#    channel = SWS.get_channel(704202325736292432)
#    await channel.send(f"{member.mention} was warned by {ctx.author.mention} with {words}")
#    await ctx.message.delete()
#    await channel.send("Sent!")

@bot.command()
#@commands.has_role (279755085943144460)
async def reply(ctx, alias, *, words):
    """Reply to a message sent to me"""
    for user_id, user_alias in bot.reply.items():
        if alias == user_alias:
            user = bot.get_user(user_id)
            await user.send(words)
            await ctx.send(f"Sent to {user.mention}")

#@bot.command()
#async def mute(ctx, member: discord.Member):
#    """Mute a user indefinitely"""
#    guild_obj = ctx.guild
#    if not member:
#        await ctx.send("Please specify a member")
#        return
#    else:
#        mute_role = guild_obj.get_role(706210954760945734)
#        await member.add_roles(mute_role)
#        await ctx.message.delete()
#        await ctx.send(f"{member.mention} was muted")

#@bot.command()
#async def tempmute(ctx, member: discord.Member, length: int):
#    """Temporarily mute a user using the time in minutes"""
#    guild_obj = ctx.guild
#    if not member:
#        await ctx.send("Please specify a member")
#        return
#    else:
#        mute_role = guild_obj.get_role(706210954760945734)
#        await member.add_roles(mute_role)
#        await ctx.message.delete()
#        await ctx.send(f"{member.mention} was muted")
#        length = length * 60
#        await asyncio.sleep(length)
#        await member.remove_roles(mute_role)
#        await ctx.send(f"{member.mention} was unmuted")

#@bot.command()
#async def unmute(ctx, member: discord.Member):
#    """Unmute a currently muted user"""
#    guild_obj = ctx.guild
#    if not member:
#        await ctx.send("Please specify a member")
#        return
#    else:
#        mute_role = guild_obj.get_role(706210954760945734)
#        await member.remove_roles(mute_role)
#        await ctx.message.delete()
#        await ctx.send(f"{member.mention} was unmuted")


#MATH-----------------------------------------------------------------------

#@bot.command()
#async def add(ctx, a: int, b: int):
#    """Add some bitches up"""
#    await ctx.send(f"{a}+{b}={a + b}")

#@bot.command()
#async def subtract(ctx, a: int, b: int):
#    """Delete some motherfuckers"""
#    await ctx.send(f"{a}-{b}={a - b}")

#@bot.command()
#async def multiply(ctx, a: int, b: int):
#    """Spread your seed"""
#    await ctx.send(f"{a}x{b}={a * b}")

#@bot.command()
#async def divide(ctx, a: int, b: int):
#    """Split up some hoes"""
#    await ctx.send(f"{a}/{b}={a / b}")

#@bot.command()
#async def power(ctx, a: int, b: int):
#    """Flex on them"""
#    await ctx.send(f"{a}^{b}={a ** b}")

#COGS----------------------------------------------------------------------------

bot.load_extension("cogs.math")
bot.load_extension("cogs.main")
#bot.load_extension("cogs.SageModeration")
#bot.load_extension("cogs.fun")

bot.run(Token)
