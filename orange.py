import discord
import numpy as np
import cv2
from random import randint
TOKEN = 'Nzc2NDA0Mzg0MTc5MTU5MDcx.X60Y7g.IvnI989n5bTH8To9bxI5CEZ2NaM'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!orange'):
        a=np.full((400,400,3),(randint(0,40),randint(80,130),240))
        cv2.imwrite("orange.png",a)
        await message.channel.send('Orange', file=discord.File('orange.png'))
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

