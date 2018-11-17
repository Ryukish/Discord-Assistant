# Discord-Bot
![PyPI](https://img.shields.io/badge/python-3.4--3.6-green.svg)
![PyPI](https://img.shields.io/badge/build-passing-green.svg)

This is for a Discord bot using the discord.py wrapper made for fun.


## Getting Started

### Installing
Install with pip for your ease:
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
```py
import asyncio
import discord
import datetime
import urllib.request, json
from urllib.request import urlopen
from discord.ext import commands

#This file will still use the same prefix of the main file to call functions
#in this case it is "!"
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
                    await self.bot.send_message(ctx.message.channel,":umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2:      :umbrella2: :umbrella2:")
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

### Music.py
### Reddit.py
### Commands && On_Message
### Background Task
