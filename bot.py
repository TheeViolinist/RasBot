import random
import discord
import os
from discord.ext import commands # Importa a classe comands do pacote discord.ext
from dotenv import load_dotenv

load_dotenv()
# Inicialização do client e intents #
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)
intents.message_content = True 

# Classe que indica o membro
class Pessoa:
    def __init__(self, nome):
        self.nome_member = nome
        self.gemidos = 0
   
class Bot:
    # Construtor do bot inicializa as configurações
    def __init__(self):
        self.membros = list()          
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

            #ctx.author retorna a classe author cujo atributo eh nick
            if(ctx.author.nick == None ):
                message = f'Hello {ctx.author.name}'
            else:
                message = f'Hello {ctx.author.nick}'
            
            await ctx.send(message)
    
    def command_gemido(self):
        @client.command()
        async def ainn(ctx):
            membro = Pessoa(ctx.author.name)
            if membro.nome_member not in self.membros:
                self.membros.append(membro.nome_member)
            else:
                membro.gemidos += 1
            
            message = f'{ctx.author.name} gemeu {membro.gemidos} vezes!'
            await ctx.send(message)
                

    def command_math(self):
        @client.command()
        async def math(ctx, number1:float , operation, number2:float):
            if(operation == '+'):
                await ctx.send(f'{number1} + {number2} = {number1 + number2}')
            elif(operation == '-'):
                await ctx.send(f'{number1} - {number2} = {number1 - number2}')
            elif(operation == '*'):
                await ctx.send(f'{number1} x {number2} = {number1 * number2}')
            elif(operation == '/'):
                await ctx.send(f'{number1} / {number2} = {number1 / number2}')
            
    def command_dice(self):
        @client.command()
        async def roll(ctx, max:int):
            number = random.randint(1, max)
            await ctx.send(number)


    
def main():
    bot = Bot()

    bot.command_dice()
    bot.command_math()
    bot.command_hello()
    bot.command_gemido()
    bot.command_run()
    

if __name__ == "__main__":
    main()








