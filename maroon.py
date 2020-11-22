import discord
import numpy as np
import cv2
from random import randint
import pickle
import os
f=open("tokens.bin",'rb')
tokens=pickle.load(f)
TOKEN = tokens['maroon']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!maroon'):
        a=np.full((400,400,3),(0,0,randint(110,130)))
        cv2.imwrite("maroon.png",a)
        await message.channel.send('maroon', file=discord.File('maroon.png'))
        os.remove("maroon.png")
    if message.content.startswith('!yellow'):
        num=randint(210,255)
        a=np.full((400,400,3),(randint(0,200),num,num))
        cv2.imwrite("yellow.png",a)
        await message.channel.send('yellow', file=discord.File('yellow.png'))
        os.remove("yellow.png")
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)