# Discord-Bot
![PyPI](https://img.shields.io/badge/python-3.4--3.6-green.svg)
![PyPI](https://img.shields.io/badge/build-passing-green.svg)

This is for a Discord bot using the discord.py wrapper made for fun.


## Getting Started

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
To use this file you will need an API key (free version gives: 1000 queries per day): [WeatherBit](https://www.weatherbit.io/api)

#### Example 1(1 Day 3 Hour Interval Forecast)
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
 
# When you run bot.py ('Weather is loaded') should be printed to console
#else if you have an error in the file(usually syntax)
def setup(bot):
    bot.add_cog(Weather(bot))
    print('Weather is loaded')
```
#### Example 2(7 Day Forecast 1 Day Interval)
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
            
# When you run bot.py ('Weather is loaded') should be printed to console
#else if you have an error in the file(usually syntax)
def setup(bot):
    bot.add_cog(Weather(bot))
    print('Weather is loaded')
```
### Music.py
```

```
### Reddit.py
To use this file you will need an API key and API wrapper(for ease): [Reddit API](https://www.reddit.com/prefs/apps)---[Reddit API Wrapper](https://github.com/praw-dev/praw)

#### Example 1(Background task to grab reddit links off subreddits of choice)
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
            
def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit is loaded')
```
#### Example 2(Making a command to grab a post off subreddit)
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

def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit is loaded')
```
#### Example 3(Making a command to grab a post off a specified subreddit)
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

def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit is loaded')
    ```
    
### Commands & On_Message
```py

```
