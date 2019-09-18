import discord
import requests
from config import *
from mcstatus import MinecraftServer
from discord.ext import commands

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
    help = ">>> **%status:** Shows if the server is online\n**%players:** Shows number of players online\n" \
           "**%craft <item>**: Shows the crafting recipe for the item"
    await ctx.channel.send(help)

# How many players are online on the server
@bot.command(name='online')
async def online(ctx):
    try:
        response = server.status().players.online
        await ctx.channel.send("There are %i players on the server" % response)
    except:
        await ctx.channel.send("Error")

# Shows crafting recipe for item, gets image from minecraftcrafting.info
@bot.command(name='craft')
async def craft(ctx, arg):
    link = "https://www.minecraftcrafting.info/imgs/craft_" + arg.lower()
    if requests.get(link + ".png").status_code != 404:
        link = link + ".png"
    elif requests.get(link + ".jpg").status_code != 404:
        link = link + ".jpg"
    elif requests.get(link + ".gif").status_code != 404:
        link = link + ".gif"
    else:
        link = "Invalid, or it has some weird name I haven't accounted for yet"
    await ctx.channel.send(link)

# Checks whether the server is online or offline and outputs the ping
@bot.command(name='status')
async def status(ctx):
    try:
        response = server.ping()
        await ctx.channel.send(":white_check_mark: Server is online with a ping of %.2fms" % response)
    except:
        await ctx.channel.send(":x: Server is offline")

bot.run(api_key)
