import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle


class InfoCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("InfoCog BOT connected")
        
    @commands.command()
    async def list_test(self, ctx):
        channel = self.client.get_channel(776863708487483432)
        
        await channel.send(
            embed = discord.Embed(
                title = 'Wanna some meme?'
            ),
            components = [
                Button(style = ButtonStyle.green, label = "Some meme"),
                Button(style = ButtonStyle.red, label = "Star Wars"),
                Button(style = ButtonStyle.blue, label = "Genshin")
            ]
        )
        

def setup(client):
    client.add_cog(InfoCog(client))