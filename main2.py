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

# TODO  Respond to any message with they key word "hal" as the first or last word
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
        try:
            # Add all found cards to a list.
            card_list = Card.where(name=card_name).array()

            # Get the last row in the array, which (theoretically) is the most recent printing.
            card = card_list[card_list.__len__() - 1]

            # Send picture of card.
            await message.channel.send(card['imageUrl'])

            # TODO  Send URL of page instead of image
        except IndexError:
            await message.channel.send("Unable to find card \"{0}\".".format(card_name))

    #  Execute script on host
   # if message.content.startswith('$doit'):
   #     pid = subprocess.Popen([sys.executable, r'C:\Users\cm\PycharmProjects\untitled\main.py'])

client.run('NTI0OTEzOTE1NDYxODk0MTU1.XLvNAA.U0_UAuKMM5_Wq3lVRiROkFUpbAM')
