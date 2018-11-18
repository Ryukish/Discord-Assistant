import discord
import os,random
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions=["Music","Weather","Reddit"]
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("bot is online")

@bot.listen()
async def on_message(message):
    if "@---BOT ID---" in message.content.lower():
        mylist =["What boy!","Yes?","Booming!!!!"]
        new_message = random.choice(mylist)
        await bot.send_message(message.channel, new_message)
        await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    if "What is up" in message.content.lower():
        await bot.send_message(message.channel,"Nothing much)
        await bot.process_commands(message)
                     
class Main_Commands():
    def __init__(self,bot):
        self.bot = bot
        
@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say("```Commands:\nhello\nhi\nping\npong\nTime\nMastercs\ncommandsm\nUGcsUH\nUHscholarship\nWeather City,Country\nBlessed: Post random memes from my folder\nBlessed5: Post 5 random memes from my folder\ndank: Goes\
 to /r/memes reddit and grabs a random post from the hot section\ndankmemes: Goes to /r/dankmemes reddit and grabs a random post from the hot section\npuppy: Goes to /r/puppies reddit and grabs\
a random post from the hot section\nokbr: Goes to /r/okbuddyretard reddit and grabs a random post from the hot section\nfunny: Goes to /r/funny reddit and grabs a random post from the hot section```")

@bot.command(pass_context=True)
async def commandsm(ctx):
    await bot.say("```For music:\nplay\npause\nresume\nsummon\nplaying\nvolume\nkillyourself```")
    
@bot.command(pass_context=True)
async def funnyPics5(ctx):
     mypath = r"C:\Users\User\Desktop\memes"
     for i in range(0,5):
         channel=ctx.message.channel.id
         choice = os.path.join(mypath, random.choice(os.listdir(mypath))) 
         await bot.send_file(discord.Object(id=channel), choice)

@bot.command(pass_context=True)
async def Blessed(ctx):
    mypath = r"C:\Users\User\Desktop\memes"
    channel=ctx.message.channel.id
    choice = os.path.join(mypath, random.choice(os.listdir(mypath))) 
    await bot.send_file(discord.Object(id=channel), choice)
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi")

@bot.command(pass_context=True)
async def Mastercs(ctx):
    await bot.say("https://ssl.uh.edu/nsm/computer-science/graduate/masters/")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('failed to load ext'.format(extension, exc))

bot.run("DISCORD TOKEN")
