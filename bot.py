import random
import discord
import os
from discord.ext import commands # Importa a classe comands do pacote discord.ext
from dotenv import load_dotenv
import youtube_dl




load_dotenv()
# Inicialização do client e intents #
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)
intents.message_content = True 


##########################
# funçẽos auxiliares    #
    # Procura se o membro está no vetor
def search_member(name, list_members):
    i = 0
    for member in list_members:
        if member.id == name: 
            return i
        i += 1
    return -1
#########################

# Classe music
class Music:
    def command_join(self):
        @client.command()
        async def join(ctx):
            if ctx.author.voice is None:
                await ctx.send("Entre em um canal de voz.")
            
            voice_channel = ctx.author.voice.channel
            
            # Se o canal de voz do cliente for nenhum, ele conecta no canal do autor, caso não ele se move
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
    
    def command_disconnect(self):
        @client.command()
        async def leave(ctx):
            await ctx.voice_client.disconnect()
    
    def command_play(self):
        @client.command()
        async def play(ctx, url):
            
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else :
                await ctx.voice_client.move_to(voice_channel)
            
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)


    def command_pause(self):
        @client.command()
        async def pause(ctx):
            await ctx.voice_client.pause()
            await ctx.send("Paused")
    
    def command_resume(self):
        @client.command()
        async def resume(ctx):
            await ctx.voice_client.resume()
            await ctx.send("Resume")
        

# Classe que indica o membro
class User:
    def __init__(self, id):
        self.id = id
        self.gemidos = 0
   
class Bot:
    # Construtor do bot inicializa as configurações
    def __init__(self):
        self.members = list()          
        self.music = Music()
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
    # Inicializa um novo membro caso ele não exista, se ele existir soma seu atributo de gemido por mais 1
    def command_gemido(self):
        @client.command()
        async def ainn(ctx):
            member = User(ctx.author.id)
            index = search_member(member.id, self.members)
            if index == -1:
                self.members.append(member)
            else:
                self.members[index].gemidos += 1
            
            message = f'{ctx.author.name} gemeu {self.members[index].gemidos} vezes!'
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

    def command_ping(self):
        @client.command()
        async def ping(ctx):
            await ctx.send(f'ping {round(client.latency * 1000)}ms')

    def command_music(self):
        self.music.command_join()
        self.music.command_disconnect()
        self.music.command_play()
        self.music.command_resume()
        self.music.command_pause()


    
    
def main():
    bot = Bot()
    
    bot.command_ping()
    bot.command_dice()
    bot.command_math()
    bot.command_hello()
    bot.command_gemido()
    bot.command_music()
    

    bot.command_run()
    

if __name__ == "__main__":
    main()








