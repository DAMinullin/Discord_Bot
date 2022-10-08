import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog BOT connected")

    @commands.command(name = 'пинг')
    async def _ping(self, ctx):
        await ctx.send('Pong!')



def setup(client):
    client.add_cog(Example(client))