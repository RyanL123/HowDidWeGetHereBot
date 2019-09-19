import discord
import requests
from config import *
from mcstatus import MinecraftServer
from discord.ext import commands
from discord.utils import get

server = MinecraftServer(server_ip, server_port)
prefix = "%"
bot = commands.Bot(command_prefix=prefix, help_command=None)

# Bot is ready
@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name="%help"))

# Help command
@bot.command()
async def help(ctx):
    help_output = ""
    help = []
    help.append(">>> **%status:** Shows if the server is online")
    help.append("**%online:** Shows number of players online")
    help.append("**%craft <item>**: Shows the crafting recipe for the item")
    help.append("**%wiki <input>:** Shows the Minecraft Wiki page for the given input")
    for i in help:
        help_output += i
        help_output += "\n\n"

    await ctx.channel.send(help_output)
    print("help")

# How many players are online on the server
@bot.command(name='online')
async def online(ctx):
    try:
        response = server.status().players.online
        await ctx.channel.send("There are %i players on the server" % response)
    except:
        await ctx.channel.send("Error")
    print("online")

# Shows crafting recipe for item, gets image from minecraftcrafting.info
@bot.command(name='craft')
async def craft(ctx, *arg):
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
        link = "Invalid, or it has some weird name I haven't accounted for yet"
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


@bot.command(name='paid')
async def paid(ctx, user: discord.user, paid_status):
    role = get(ctx.server.roles, name="Paid")
    if paid_status.upper() == "PAID":
        await bot.add_role(user, role)
    else:
        await bot.remove_role(user, role)


bot.run(api_key)
