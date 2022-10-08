import os
from random import choice

import discord
import praw
from discord.ext import commands
from discord_components import Button
from discord_components import ButtonStyle
from dotenv import load_dotenv

load_dotenv()
#935875434774683738

class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = praw.Reddit(client_id = os.getenv("ID"),
                                  client_secret = os.getenv("SECRET"),
                                  password = os.getenv("PASSWORD"),
                                  user_agent = os.getenv("USER_AGENT"),
                                  username = os.getenv("USERNAME"))
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Reddit BOT connected")

    @commands.command()
    async def meme(self, ctx, subreddit_ = "memes"):
        #добавить параметр отвечающий за количество
        author = ctx.message.author
        if author == self.client:
            return
        subreddit = self.reddit.subreddit(subreddit_)
        first40 = subreddit.top(limit = 40)
        all_subs = list(first40)
        
        random_memes = choice(all_subs)
        embed_ = discord.Embed(title = random_memes.title,
                               colour = discord.Colour.green())
        embed_.set_image(url = random_memes.url)
        
        await ctx.send(embed = embed_)
        
    @commands.command()
    async def menu_(self, ctx):
        #сделать в одном модуле, а в этом отслеживать нажатия
        await ctx.send(
            embed = discord.Embed(
                title = 'Wanna some meme?'
            ),
            components = [
                Button(style = ButtonStyle.green, label = "Some meme"),
                Button(style = ButtonStyle.red, label = "Star Wars"),
                Button(style = ButtonStyle.yellow, label = "Genshin")
            ]
        )
        
        response = await self.client.wait_for("button_click")
        if response.component.label == "Accept":
            print(1)



def setup(client):
    client.add_cog(Reddit(client))
