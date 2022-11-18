import random
import discord
import os
from discord.ext import commands # Importa a classe comands do pacote discord.ext
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as{0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Hello"):
        await message.channel.send('Hello!')

@client.command()
async def rolll(ctx, max):
    number = random.randint(1,max)
    await ctx.send(number)


client.run(os.getenv("TOKEN"))


