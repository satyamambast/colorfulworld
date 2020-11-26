import discord
import numpy as np
import cv2
from random import randint
from discord.ext import commands
import pickle
import os
def createimage(lower,upper,filename):
    a=np.full((400,400,3),(randint(lower,upper), randint(200,255), randint(200,255)))
    cv2.imwrite(filename,a)
    cv2.imread(filename)
    img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    cv2.imwrite(filename,img)

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
        createimage(21,40,"yellow.png")
        await message.channel.send('yellow', file=discord.File('yellow.png'))
        os.remove("yellow.png")
    if message.content.startswith('!blue'):
        a=np.full((400,400,3),(randint(80,255),0,0))
        cv2.imwrite("maroon.png",a)
        await message.channel.send('maroon', file=discord.File('maroon.png'))
        os.remove("maroon.png")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)