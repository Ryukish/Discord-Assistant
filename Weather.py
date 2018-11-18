import asyncio
import discord
import datetime
import urllib.request, json
from urllib.request import urlopen
from discord.ext import commands


class Weather:
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(pass_context=True)
    async def weather(self, ctx):
        location = ctx.message.content
        cold=False
        rain=False
        if location[9].lower() =='c':
            location = location[14:]
            cold=True
        elif location[9].lower()=='r':
            location = location[14:]
            rain=True
        else:
            location = location[8:]

        myarr = location.split()
        url = "https://api.weatherbit.io/v2.0/forecast/3hourly?city="+myarr[0]+"&country="+myarr[1]+"&days=1&units=I&key=YOUR-API-KEY-HERE"
        #Getting data from url and loading into json format in python
        response = urlopen(url)
        d = response.read().decode()
        data = json.loads(d)

        if cold == True:
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
                temp_temp= float(temp)
                if temp_temp<=45.0:
                    await self.bot.send_message(ctx.message.channel,":snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: ")
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

        elif rain == True:
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
                temp_pop = int(pop)
                if temp_pop >= 50:
                    await self.bot.send_message(ctx.message.channel,":umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2:")
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

        else:
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
                temp_pop = int(pop)
                temp_temp= float(temp)
                if temp_pop >= 50:
                    await self.bot.send_message(ctx.message.channel,":umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2: :umbrella2:")
                if temp_temp<=45.0:
                    await self.bot.send_message(ctx.message.channel,":snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: ")
                
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

        
def setup(bot):
    bot.add_cog(Weather(bot))
    print('Weather is loaded')
