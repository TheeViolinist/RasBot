import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Olá, estou conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


bot.run(os.getenv("TOKEN"))
