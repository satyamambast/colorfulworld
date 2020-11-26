import discord
from discord.ext import commands
import numpy as np
import cv2
from random import randint
import pickle
import os
f=open("tokens.bin",'rb')
tokens=pickle.load(f)
TOKEN = tokens['orange']
client = commands.Bot(command_prefix=["! ","!"])

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     if message.content.startswith('!orange'):
#         a=np.full((400,400,3),(randint(0,40),randint(80,130),240))
#         cv2.imwrite("orange.png",a)
#         await message.channel.send('orange', file=discord.File('orange.png'))
#         os.remove("orange.png")
@client.command()
async def orange(ctx):
    a=np.full((400,400,3),(randint(0,40),randint(80,130),240))
    cv2.imwrite("orange.png",a)
    ctx.send('orange', file=discord.File('orange.png'))
    os.remove("orange.png")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

