import random
import discord
import os
from discord.ext import commands # Importa a classe comands do pacote discord.ext
from dotenv import load_dotenv

load_dotenv()
# Inicialização do client e intents #
intents = discord.Intents.default()
<<<<<<< HEAD
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)
=======
client = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True 

class Bot:
    # Construtor do bot inicializa as configurações
    def _init_(self):            
        @client.event
        async def on_ready():
            print('We have logged in as{0.user}'.format(client))


    def command_run(self):
        client.run(os.getenv("TOKEN"))


    def command_hello(self):
        #o nome da função será aquela chamada pelo prefixo de comando que invoca a função, ela deve ter ao menos um parâmetro ctx que é o Context do bot.
        # O context representa todo o conteúdo de onde o commando foi dado, servidor, autor, context.send envia uma mensagem para onde o comando foi invocado
        @client.command()
        async def hello(ctx):
            message = f'Hello {ctx.author.nick}!'
            await ctx.send(message)

    
    
def main():
    bot = Bot()

    bot.command_hello()
    bot.command_run()


if __name__ == "__main__":
    main()



>>>>>>> 02c0428000ba2d1b52b1f2f4ee77b93cfc1e33b0


@client.command()
async def rolll(ctx, max):
    number = random.randint(1,max)
    await ctx.send(number)




