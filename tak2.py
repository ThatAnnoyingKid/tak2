import discord
import os

from christan import no_bad_words

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

print("Starting up bot...")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try: # I am poor with only one monitor so I can see when I want to kill myself faster this way
         judgement = no_bad_words(message)
         if judgement == True:
              await message.channel.send(file=discord.File('christan.png'))
    except Exception as e:
        await message.channel.send(e)

client.run(os.environ["TOKEN"])