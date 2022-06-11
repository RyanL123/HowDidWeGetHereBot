# HowDidWeGetHere Bot

This bot was created to assist in a private
Minecraft Discord Server. It has many utility
functions that only work for 
the specific server and is not configurable. The aim of 
the Minecraft Server is to obtain every achievement,
including the hidden "How Did We Get Here?" achievement.

# Installation

1. Create .env file
2. Populate with server and bot token
```
server_ip=SERVER_IP
server_port=SERVER_PORT
api_key=API_KEY
```
3. Run the bot
```
docker-compose up
```


# Commands (Used with % prefix)

## Show Server Status (%status)

### Parameters (None)

### Functionality

**What it does**

- Shows whether if the server is online or offline
- Shows the ping of the server
- Shows the names of every player in the server


**What it can't do**

- Get the status of any other server (not configurable)
- Get the total uptime of the server

**Output**
> :white_check_mark: Server is online with a ping of (milliseconds) ms
>
>There are x/25 max players on the server:
>
> Player1
>
> Player2
>
> ...

Or 

> :x: Server is offline

## Show Recipe (%craft)

### Parameters (Item)

**Item:** Item you want to get the recipe for

### Functionality

**What it does**

- Show the crafting recipe of the given item
- Might not work for some items such as quartz block 
(labeled as blockofquartz instead)

**What it can't do**

- Show potion brewing recipes
- Craft uncraftable items (example: bell)
- Fix your spelling mistakes (item name must be spelt correctly)

**Output**
> www.minecraftcrafting.info/imgs/craft_ + (item name) + (file extension)

## Show Minecraft Wiki (%wiki)

### Parameters (Input)

**Input:** Thing you want to get wiki page for

### Functionality

**What it does**

- Show the official Minecraft Wiki page for the given input

**What it can't do**

- Get specific metadata from a web page
- Fix your spelling mistakes (spelling must be exact same as wiki)

**Output**
>  https://minecraft.gamepedia.com/ + (input)

## Show people committing tax fraud (%paid)

### Parameters (None)

### Functionality

**What it does**

- Display everyone who doesn't have the paid role
- Automatically removes everyone's paid role at the start of the month

**What it can't do**

- Give people the paid role
- Arrest them

**Output**
> @HowDidWeGetHereBot has not paid this month!

Or

> :tada: Everybody paid this month!

## Show latest update (%update)

### Parameters (None)

### Functionality

**What it does**

- Show the latest update to the bot

**What it can't do**

- Check any patches other than the latest update


### Alternatively, run the %help command to see what each command does.