import os

import discord
from discord.ext import commands
from discord_components import DiscordComponents
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = '!')
# client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    DiscordComponents(client)
    print("Main BOT connected")

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f"commands.{filename[:-3]}")


if __name__ == '__main__':
    client.run(os.getenv("KEY"))
