import discord
import numpy as np
import cv2
from random import randint
from discord.ext import commands
import pickle
import os
import re
def createimage(lower,upper,filename):
    a=np.full((400,400,3),(randint(lower,upper), randint(200,255), randint(200,255)))
    cv2.imwrite(filename,a)
    img=cv2.imread(filename)
    img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    cv2.imwrite(filename,img)
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return  tuple([int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)][::-1])

f=open("tokens.bin",'rb')
tokens=pickle.load(f)
TOKEN = tokens['maroon']

client = commands.Bot(command_prefix=["! ","!"])


@client.command()
async def maroon(ctx):
    a=np.full((400,400,3),(0,0,randint(110,130)))
    cv2.imwrite("maroon.png",a)
    await ctx.send('maroon', file=discord.File('maroon.png'))
    os.remove("maroon.png")

@client.command()
async def yellow(ctx):
    createimage(25,35,"yellow.png")
    await ctx.send('yellow', file=discord.File('yellow.png'))
    os.remove("yellow.png")

@client.command()
async def blue(ctx):
    a=np.full((400,400,3),(randint(40,255),0,0))
    cv2.imwrite("blue.png",a)
    await ctx.send('blue', file=discord.File('blue.png'))
    os.remove("blue.png")

@client.command(aliases=['color','clr'])
async def colour(ctx,hex):
    if re.match(r'^#{0,1}[0-9A-F]{6}$',hex,re.I):
        clr=hex_to_rgb(hex)
        a=np.full((400,400,3),clr)
        cv2.imwrite("colour.png",a)
        await ctx.send(hex, file=discord.File('colour.png'))
        os.remove("colour.png")
    else:
        await ctx.send("Invalid Hex : Please only enter six digit hex with a single #")
        

        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)