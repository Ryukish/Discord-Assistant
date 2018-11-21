# Discord-Bot
![PyPI](https://img.shields.io/badge/python-3.4--3.6-green.svg)
![PyPI](https://img.shields.io/badge/build-passing-green.svg)

This is for a Discord bot using the discord.py wrapper made for fun.


## Getting Started
##### Weather.py: 
```
!weather: 1 Day 3 Hour Interval Forecast
!forecast: 7 Day Forecast 1 Day Interval
```
##### Reddit.py
```
Background_Task: Used to send random reddit post to a specific user on a 3 hour interval
!puppy: Goes to /r/puppies reddit and grabs a random post from the hot section
```
##### Music.py:
```
!summon: Bot will join the voice channel of the user who summoned it
!play: Takes in a youtube link or title of video and plays the audio of the video
!volume: Controls the volume of the bot(default set to 60%)
!pause: Pauses the current song that is playing and waits
!resume: Continues the song if it was paused 
!EndAll: Clears the queue and the bot leaves the voice channel
!skip: Skips the current song playing 
!playing: Give the title of the current song playing
```
##### Bot.py
```
On_message: These type of commands will look for a keywords or phrase inside all the messages sent on discord
!ping: The bot prints 'pong'
!hello: The bot prints 'hi'
!MasterThis: This command would print a link that would be specific in the code
```

### Installing
Installation can be completed using the following pips:
```
pip install -U discord.py[voice]    
pip install --upgrade youtube-dl 
pip install praw  
```

## Built With
* [Discord](https://discordapp.com/developers/applications/) - Used connect the bot to Discord
* [WeatherBit](https://www.weatherbit.io/api) - The API used to get Weather Data in a JSON format
* [Reddit](https://www.reddit.com/prefs/apps) - Used to connect the Discord bot to reddit
* [Discord.py API Wrapper](https://github.com/Rapptz/discord.py) - API wrapper to allow for python written discord bot
* [Youtube-dl](https://github.com/rg3/youtube-dl) - Used to get Youtube videos to play through discord bot
* [Reddit API Wrapper](https://github.com/praw-dev/praw) - API wrapper to allow for python written reddit scripts

## Explanations and Examples

### Weather.py
To use this file you will need an API key (free version gives: 1000 queries per day)
* [WeatherBit](https://www.weatherbit.io/api) - The API used to get Weather Data in a JSON format

#### Header 
```py
import asyncio
import discord
import datetime
import urllib.request, json
from urllib.request import urlopen
from discord.ext import commands

#This file will still use the same prefix of the main file to call functions
#in this case it is "!" (check bot.py to see the prefix or change it)
class Weather:
    def __init__(self, bot):
        self.bot = bot
        

  ---- Functions & Classes of the Weather.py ----


# When you run bot.py ('Weather is loaded') should be printed to console
#else if you have an error in the file(usually syntax)
def setup(bot):
    bot.add_cog(Weather(bot))
    print('Weather is loaded')
```

#### Example 1(1 Day 3 Hour Interval Forecast)
```py      
    #must me commands.commands due to this file being a cog of the main bot.py file
    #for more information on cogs: https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5
 
    @commands.command(pass_context=True)
    async def weather(self, ctx):   #This is how you would call this function "!weather Houston US"(City Country)
        location = ctx.message.content #This will get the whole message("!weather Houston US") 
        location = location[8:] #Gets rid of ("!weather ") in the string
        myarr = location.split() #Split it into ([city,country])
        
        #The url format tells you the data it will get, for this example it will go to (5-days 3h-interval) data and get 1 day
        #https://www.weatherbit.io/api/swaggerui/weather-api-v2#/ <---will show you how to create a link
        
        url = "https://api.weatherbit.io/v2.0/forecast/3hourly?city="+myarr[0]+"&country="+myarr[1]+"&days=1&units=I&key=YOUR-API-KEY-HERE"
        #Getting data from url and loading into json format in python
        response = urlopen(url)
        d = response.read().decode()
        data = json.loads(d)
        
        #Gets data from 6:00 A.M. - 9:00 P.M.(local time of location)
        # In Imerpial units
        for x in range(1,7):
                dt = str(data['data'][x]['timestamp_local'])
                dt = dt[:10] +' '+dt[11:]
                temp= str(data['data'][x]['temp'])
                tempA= str(data['data'][x]['app_temp'])
                snow=str(data['data'][x]['snow'])
                pop=str(data['data'][x]['pop'])
                precip=str(data['data'][x]['precip'])
                hum=str(data['data'][x]['rh'])
                weath=str(data['data'][x]['weather']['description'])
                
                #converts strings into int
                temp_pop = int(pop)
                temp_temp= float(temp)
                
                #if Chance of Rain is great than 50% output a sign(umbrella emotes in this case)
                if temp_pop >= 50:
                    await self.bot.send_message(ctx.message.channel,":umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2:   :umbrella2: :umbrella2:")
                #if tempature is less than 45.0 F output a sign(snowflake emotes in this case)
                if temp_temp<=45.0:
                    await self.bot.send_message(ctx.message.channel,":snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: ")
                
                #Using embedded message to give it a nice format
                embed=discord.Embed(title="Location", description=myarr[0]+","+ myarr[1], color=discord.Color(0x0ae1fd))
                embed.set_author(name="Weather Forecast Today")
                embed.add_field(name="Weather Discription", value=weath, inline=True)
                embed.add_field(name="Date Time", value=dt, inline=True)
                embed.add_field(name="Temperature", value=str("Temp: "+temp+"\nApp Temp: "+tempA), inline=True)
                embed.add_field(name='Precipitation', value=str(precip+"%"), inline=True)
                embed.add_field(name='Snow', value=str(snow+"%"), inline=True)
                embed.add_field(name='Chance of Rain', value=str(pop+"%"), inline=True)
                embed.add_field(name='Humidity', value=str(hum+"%"), inline=True)
                await self.bot.send_message(ctx.message.channel,embed=embed)
```
#### Example 2(7 Day Forecast 1 Day Interval)
```py

#This file will still use the same prefix of the main file to call functions
#in this case it is "!" (check bot.py to see the prefix or change it)      

    @commands.command(pass_context=True)
    async def forecast(self,ctx):
        location = ctx.message.content
        location = location[9:]
        myarr = location.split()
        
        #The url format tells you the data it will get, for this example it will go to (16-days 1D-interval) data and gets 7 day
        #https://www.weatherbit.io/api/swaggerui/weather-api-v2#/ <---will show you how to create a link
        
        url = "https://api.weatherbit.io/v2.0/forecast/daily?city="+myarr[0]+"&country="+myarr[1]+"&units=I&key=YOUR-API-KEY-HERE"
        
        #Getting data from url and loading into json format in python
        response = urlopen(url)
        d = response.read().decode()
        data = json.loads(d)
        
        #Gets data for 7 days(local time of location)
        # In Imerpial units
        for x in range(0,7):
            dt = str(data['data'][x]['datetime'])
            tempMax= str(data['data'][x]['max_temp'])
            tempMin= str(data['data'][x]['app_min_temp'])
            tempAMax= str(data['data'][x]['app_max_temp'])
            tempAMin= str(data['data'][x]['app_max_temp'])
            snow=str(data['data'][x]['snow'])
            pop=str(data['data'][x]['pop'])
            precip=str(data['data'][x]['precip'])
            hum=str(data['data'][x]['rh'])
            weath=str(data['data'][x]['weather']['description'])
            
            #Using embedded message to give it a nice format
            embed=discord.Embed(title="Location", description=myarr[0]+","+ myarr[1], color=discord.Color(0x0ae1fd))
            embed.set_author(name="Weather Forecast")
            embed.add_field(name="Weather Discription", value=weath, inline=True)
            embed.add_field(name="date time", value=dt, inline=True)
            embed.add_field(name="Temperature", value=str("Max Temp: "+tempMax+"\nMin Temp: "+tempMin+"\nMax App Temp: "+tempAMax+"\nMin App Temp: "+tempAMin), inline=True)
            embed.add_field(name='Precipitation', value=str(precip+"%"), inline=True)
            embed.add_field(name='Snow', value=str(snow+"%"), inline=True)
            embed.add_field(name='Chance of Rain', value=str(pop+"%"), inline=True)
            embed.add_field(name='Humidity', value=str(hum+"%"), inline=True)
            await self.bot.send_message(ctx.message.channel,embed=embed)           
```
### Reddit.py
To use this file you will need an API key and API wrapper(for ease). 
* [Reddit API Wrapper](https://github.com/praw-dev/praw)
* [Reddit API Wrapper](https://github.com/praw-dev/praw) - API wrapper to allow for python written reddit scripts

#### Header
```py
import discord
import random
import asyncio
import praw
from discord.ext import commands

#You can get Client_id/Client_secret/User_agent from the url below
#https://www.reddit.com/prefs/apps
#You need to create a reddit application to get this infomation

reddit = praw.Reddit(client_id='XXXXXXXXXXX',
                     client_secret='XXXXXXXXXXXXXXXXXXX',
                     user_agent='Name of the application')

class Reddit:
    def __init__(self, bot):
        self.bot = bot
        
        
---- Functions & Classes of the Reddit.py ----

def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit is loaded')
```
        
#### Example 1(Background task to grab reddit links off subreddits of choice)
```py
class Reddit:
    def __init__(self, bot):
        self.bot = bot
        #Starts the loops so that it will run constantly while the bot.py is running
        self.bot.loop.create_task(self.background_task())
        self.bot.loop.create_task(self.dm_task())

    async def background_task(self):
        await self.bot.wait_until_ready()
        
        #The channel id can be gotten from discord when you right click a channel(Must have developer mode on in discord)
        channel = discord.Object(id='-----channel id-----')
        #Makes so it doesn't start for 1 hour(3600 seconds/ 60 mins = 1 hour)
        #Runs in seconds 
        await asyncio.sleep(3600)
        while not self.bot.is_closed:
           #while the bot.py is still running, do this
           
           #Decides what subreddit you are going to
            mes = reddit.subreddit('memes').hot()
            
            #picks a post from the top 20
            post_to_pick = random.randint(1, 20)
            
            #Goes to /r/memes reddit and grabs a random post from the hot section
            for i in range(0, post_to_pick):
                submission = next(x for x in mes if not x.stickied)
            await self.bot.send_message(channel, submission.url)
            
            #sleeps for 1 hour then repeats
            await asyncio.sleep(3600)
            
    async def dm_task(self):
        await self.bot.wait_until_ready()
        hi = await self.bot.get_user_info('----USER ID----')
        
        #sleeps for 3h ours then starts
        await asyncio.sleep(10800)
        
        while not self.bot.is_closed:
            #while the bot.py is still running, do this
            
            #Decides what subreddit you are going to
            mes = reddit.subreddit('memes').hot()
            
            #picks a post from the top 20
            post_to_pick = random.randint(1, 20)
            
            #Goes to /r/memes reddit and grabs a random post from the hot section
            for i in range(0, post_to_pick):
                submission = next(x for x in mes if not x.stickied)
                
            #The bot sends a private Message to the User
            await self.bot.send_message(hi, submission.url)
            
            #Sleeps for 3 hours and repeats
            await asyncio.sleep(10800)
```
#### Example 2(Making a command to grab a post off subreddit)
```py
    #allows for the prefix set in Bot.py to work to call this function
    @commands.command(pass_context=True)
    async def puppy(self):
        #Decides what subreddit you are going to
        pup = reddit.subreddit('puppies').hot()
        
        #picks a post from the top 20
        post_to_pick = random.randint(1, 20)
        
        Goes to /r/puppy reddit and grabs a random post from the hot section
        for i in range(0, post_to_pick):
            submission = next(x for x in pup if not x.stickied)
        await self.bot.say(submission.url)
```
#### Example 3(Making a command to grab a post off a specified subreddit)
```py
    #allows for the prefix set in Bot.py to work to call this function
    @commands.command(pass_context=True)
    async def redditThis(self,ctx):
        
        #!redditThis puppy
        subreddit = ctx.message.content
        #Getting rid of "!redditThis "
        subreddit = subreddit[12:]
        
        #Decides what subreddit you are going to
        pup = reddit.subreddit(subreddit).hot()
        
        #picks a post from the top 20
        post_to_pick = random.randint(1, 20)
        
        Goes to specified reddit and grabs a random post from the hot section
        for i in range(0, post_to_pick):
            submission = next(x for x in pup if not x.stickied)
        await self.bot.say(submission.url)
```
### Music.py
You will use Youtube-dl to download the videos into the queue(ffmpeg.exe).
Discord api wrapper provides the framework to get the bot to join channels and play music/queue up music.
* Youtube-dl - Used to get Youtube videos to play through discord bot
* Discord.py API Wrapper - API wrapper to allow for python written discord bot

#### Header
```py
import asyncio
import discord
from discord.ext import commands
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


def __init__(self, bot):
        self.bot = bot
        
        
      ---- Functions & Classes of the Music.py ----
        
def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')
 ```
 #### Class VoiceEntry
 ```py
 class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)
 ```
 #### Class VoiceState
 ```py
 class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set()
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
  ```
#### Class Music
```py
class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Already in a voice channel...')
        except discord.InvalidArgument:
            await self.bot.say('This is not a voice channel...')
        else:
            await self.bot.say('Ready to play audio in **' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('Not in a channel boi!!')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            await self.bot.say("Loading the song please be patient..")
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))
            
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

            
    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        server = ctx.message.server
        state = self.get_voice_state(server)
        if state.is_playing():
            player = state.player
            player.pause()
            tell=0;
            
    @commands.command(pass_context=True, no_pm=True)
    async def EndAll(self, ctx):
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say("Cleared the queue and disconnected from voice channel")
        except:
            pass


    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('Not playing any music right now...')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('Requester requested skipping song...')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            await self.bot.say('Skip vote passed, skipping song...')
            state.skip()
        else:
            await self.bot.say('You have already voted to skip this song.')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('Not playing anything.')
        else:
            skip_count = len(state.skip_votes)
            
```            
### Commands & On_Message
#### On_Message(No need for prefix("!command") use if you use these)
```py
#If you mention or @ the bot it will pick a random relpy from the list and print it
@bot.listen()
async def on_message(message): 
    if "@---ID OF THE BOT---" in message.content.lower():
        mylist =["Yes?","Hello!!"]
        new_message = random.choice(mylist)
        await bot.send_message(message.channel, new_message)
        await bot.process_commands(message)

#Will find the given message in a sentence with out the command prefixs.
@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    if "What is up guys" in message.content.lower():
        await bot.send_message(message.channel,"Nothing much")
        await bot.process_commands(message)
```
#### Commmands(Commands use the specific bot prefix you define to call these(!hello), "!" is the prefix)
```py
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi")

@bot.command(pass_context=True)
async def FunnyStuff(ctx):
    mypath = r"C:\Users\Desktop\funny"
    channel=ctx.message.channel.id
    choice = os.path.join(mypath, random.choice(os.listdir(mypath))) 
    await bot.send_file(discord.Object(id=channel), choice)
```
