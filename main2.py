import discord
import sys
import subprocess
from mtgsdk import Card

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("01101111011101100110111001101001")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$openthedoor'):
        await message.channel.send("I'm sorry, I cannot do that.")

    if message.content.startswith('$whisper'):
        await message.author.send("Hello %s." % message.author)

    if message.content.startswith('$goodnight'):
        await message.channel.send("Good night, %s.  Rest in peace." % message.author)

    if message.content.startswith('$card'):
        card_name = message.content[6:]
        card = Card.where(name=card_name).all()
        if not card:
            await message.channel.send('Error: cannot find card {0.content}'.format(client))
        else:
            if card[0].image_url is None:
                await message.channel.send(card[1].image_url)
            else:
                await message.channel.send(card[0].image_url)

        #fmt = '{0.author.name} has deleted the message:\n{0.content}'
        #await message.author.send(fmt.format(message))



   # if message.content.startswith('$doit'):
   #     pid = subprocess.Popen([sys.executable, r'C:\Users\cm\PycharmProjects\untitled\main.py'])

client.run('')
