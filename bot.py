import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Olá, estou conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


bot.run("MTA0MTAxODk5MTYwMDIxMDA1Mg.GOOtMx.xAu1MI7HQPJ5FNya-CkGxWNzjLU9M_8XlNP0xM")
