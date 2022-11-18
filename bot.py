<<<<<<< HEAD
=======
import discord
import os
from discord.ext import commands # Importa a classe comands do pacote discord.ext
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as{0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Hello"):
        await message.channel.send('Hello!')


client.run(os.getenv("TOKEN"))


>>>>>>> 515f04c2834b71c471cc0c824e68f78717540221
