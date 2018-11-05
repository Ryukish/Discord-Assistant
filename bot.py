import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions=["Music"]
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("bot is online boi!!!")

class Main_Commands():
    def __init__(self,bot):
        self.bot = bot

@bot.command(pass_context=True)
async def Commands(ctx):
    await bot.say("Commands->hello/hi/ping/pong/Time/Mastercs/commandM/UGcsUH/UHscholarship")

@bot.command(pass_context=True)
async def commandsM(ctx):
    await bot.say("For music->Play/pause/resume/summon/stop/playing/volume")
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")

@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say("ping")

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi")

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hello")

@bot.command(pass_context=True)
async def Time(ctx):
    await bot.say("Activate the trap card")

@bot.command(pass_context=True)
async def Mastercs(ctx):
    await bot.say("https://ssl.uh.edu/nsm/computer-science/graduate/masters/")

@bot.command(pass_context=True)
async def UGcsUH(ctx):
    await bot.say("https://ssl.uh.edu/nsm/computer-science/undergraduate/programs/bs-cs/")

@bot.command(pass_context=True)
async def UHscholarship(ctx):
    await bot.say("https://ssl.uh.edu/nsm/computer-science/undergraduate/scholarships/")
    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('failed to load ext'.format(extension, exc))

bot.run("token id here")
