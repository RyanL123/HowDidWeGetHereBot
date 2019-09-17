import discord
from mcstatus import MinecraftServer

server = MinecraftServer("142.234.204.92", 32436)
status = server.status()
# query = server.query()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))


@client.event
async def on_message(message):
    if message.content == "%status":
        try:
            response = server.ping()
            await message.channel.send(":white_check_mark: Server is online with a ping of %.2fms" % response)
        except:
            await message.channel.send(":x: Server is offline")
    if message.content == "%help":
        await message.channel.send("> **%status:** shows if the server is online")
        await message.channel.send("> **%players:** shows number of players online")
    if message.content == "%players":
        await message.channel.send("There are %i players on the server" % status.players.online)
    # if message.content == "%players":
    #     await message.channel.send("The server has the following players online: {0}".format(", ".join(query.players.names)))

client.run('NTA3MzU1NjQ2MzIwOTY3Njgy.XX_Nbw.QM51zAdqPp-X8xJxxy7_PxMZ8Ys')