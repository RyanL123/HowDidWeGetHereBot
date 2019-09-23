import discord
import requests
from config import *
from mcstatus import MinecraftServer
from discord.ext import commands, tasks
from discord.utils import get
import datetime

server = MinecraftServer(server_ip, server_port)
prefix = "%"
bot = commands.Bot(command_prefix=prefix, help_command=None)

# Bot is ready
@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name="%help | %update"))
    test.start()

# Help command
@bot.command()
async def help(ctx, arg="default"):
    if arg == "default":
        file = open("help_text/help_default.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "online":
        file = open("help_text/help_online.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "craft":
        file = open("help_text/help_craft.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "wiki":
        file = open("help_text/help_wiki.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "status":
        file = open("help_text/help_status.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "update":
        file = open("help_text/help_update.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    elif arg == "paid":
        file = open("help_text/help_paid.txt", "r")
        data = file.read()
        await ctx.channel.send(data)
    else:
        help.append("No such command")

    print("help")

# How many players are online on the server
@bot.command(name='online')
async def online(ctx):
    try:
        response = server.status().players.online
        if response == 1:
            await ctx.channel.send("There is 1 player on the server")
        else:
            await ctx.channel.send("There are %i players on the server" % response)
    except:
        await ctx.channel.send("Error")
    print("online")

# Shows crafting recipe for item, gets image from minecraftcrafting.info
@bot.command(name='craft')
async def craft(ctx, *arg):
    if len(arg) != 0 and arg[0].upper() == "BELL":
        file = open("help_text/craft_bell.txt", "r")
        data = file.read().replace("\n", "")
        await ctx.channel.send(data)
        return
    ending = ""
    for i in range(len(arg)):
        ending += arg[i].lower()
    link = "https://www.minecraftcrafting.info/imgs/craft_" + ending
    if requests.get(link + ".png").status_code != 404:
        link += ".png"
    elif requests.get(link + ".jpg").status_code != 404:
        link += ".jpg"
    elif requests.get(link + ".gif").status_code != 404:
        link += ".gif"
    else:
        link = "Please try again"
    await ctx.channel.send(link)
    print("craft")

# Checks whether the server is online or offline and outputs the ping
@bot.command(name='status')
async def status(ctx):
    try:
        response = server.ping()
        await ctx.channel.send(":white_check_mark: Server is online with a ping of %.2fms" % response)
    except:
        await ctx.channel.send(":x: Server is offline")
    print("status")


# Shows the Minecraft wiki page for the given argument
@bot.command(name='wiki')
async def status(ctx, *arg):
    ending = ""
    # add underscores to separate words
    for i in range(len(arg)):
        ending += arg[i].lower().capitalize()
        if i != len(arg)-1:
            ending += "_"

    link = "https://minecraft.gamepedia.com/" + ending
    if requests.get(link).status_code != 404:
        await ctx.channel.send(link)
    else:
        await ctx.channel.send("Please try again")
    print("wiki")

# Notifies everyone who hasn't paid this month yet
@bot.command(pass_contex=True)
async def paid(ctx):
    message_server = ctx.message.guild

    # Initialize roles
    bot_id = get(message_server.roles, name="Bot")
    paid_id = get(message_server.roles, name="Paid")
    all_paid = True

    # Iterates through every member and check for their paid role. Ignores bots
    for member in message_server.members:
        if bot_id not in member.roles and paid_id not in member.roles:
            member_id = member.id
            await ctx.channel.send("<@%i> has not paid this month!" % member_id)
            all_paid = False
    if all_paid:
        await ctx.channel.send(":tada: Everybody paid this month!")


# @bot.command(name='role', pass_context=True)
# async def give_role(ctx, member: discord.Member):
#     message_server = ctx.message.guild
#     member_id = member.id
#     for i in message_server.members:
#         if i.id == member_id:
#             role = get(message_server.roles, name="Test")
#             await i.add_roles(role)
#             break

@bot.command()
async def update(ctx):
    file = open("help_text/latest_patch.txt", "r")
    data = file.read()
    await ctx.channel.send(data)

# Removes every paid role at the 10th of every month
async def remove_all():
    message_server = get(bot.guilds, name="How Did We Get Here?")
    role = get(message_server.roles, name="Paid")
    for i in message_server.members:
        if role in i.roles:
            await i.remove_roles(role)


@tasks.loop(hours=1)
async def test():
    time = datetime.datetime.now()
    hour = int(time.hour)
    day = int(time.day)
    if day == 10 and hour == 1:
        await remove_all()


bot.run(api_key)
