import discord
import os

from message_handeling import format_message

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

    if message.content.startswith('$'):
        await message.channel.send('Hello!')

    try: # I am poor with only one monitor so I can see when I want to kill myself faster this way
         await message.channel.send(format_message(message))
    except Exception as e:
        await message.channel.send(e)

client.run(os.environ["TOKEN"])