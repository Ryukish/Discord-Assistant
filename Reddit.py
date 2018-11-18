import discord
import os,random
import asyncio
import praw
from discord.ext import commands

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


    @commands.command(pass_context=True)
    async def funny(self):
        funny = reddit.subreddit('funny').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in funny if not x.stickied)
        await self.bot.say(submission.url)
    
            
def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit is loaded')
