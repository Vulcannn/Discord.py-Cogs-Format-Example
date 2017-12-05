#!/usr/bin/env python3.5
import discord
import asyncio
import json
from discord.ext import commands
from config import *


#with open('config.json') as json_data_file:
    #data = json.load(json_data_file)


bot = commands.Bot(command_prefix=prefix, description = description)
ext_commands = ["main"]
client = discord.Client()




@bot.event
async def on_ready():
    #with open('config.json') as json_data_file:
        #data = json.load(json_data_file)

    print("Bot Logged in!")
    owner = await bot.get_user_info('211098424655740929')
    await bot.send_message(owner, "Bot has came online!")
    await bot.change_presence(game=(discord.Game(name=status)))
    for i in range(len(ext_commands)+1):
        bot.load_extension(ext_commands[i-1])



def load_cogs(bot):
    defaults = ("main")

bot.run(token)
