import discord
from discord.ext import commands

class RandomStuff(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("RandomStuff BOT connected")

    @commands.command(aliases = ['прием', 'приём'])
    async def priem(self, ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention} На связи!')

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Нет")

    @commands.command(name = 'команды')
    async def _commands(self, ctx):
        await ctx.send("Отстань")

    @commands.command(aliases = ['bb', 'пока'])
    async def _bb(self, ctx, name = '150244723255148544'):
        await ctx.send(f'Пока <@{name}>!')

    @commands.command(name = 'кумса')
    async def kymsa(self, ctx, target = ''):
        if target:
            await ctx.send(f'Сделац кусь {target}')
        else:
            author = ctx.message.author
            await ctx.send(f'Сделац кусь {author}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        channel = self.client.get_channel(776863708487483432)
        if message.content.lower() == "who sus":
            with open('sus.jpg', 'rb') as file:
                my_file = discord.File(file)
                await message.channel.send("SUS", file = my_file)

        if 'where' in message.content.lower() and message.author != self.client.user:
            await channel.send('where \nwhere \nwhere')

        if any(elem in message.content.lower() for elem in ['ta', 'tili', 'тылита']):
            await channel.send('https://www.youtube.com/watch?v=-79oQ5xR7s0')

        if any(elem in message.content.lower() for elem in ['welcome', 'rice', 'field']):
            await channel.send('https://www.youtube.com/watch?v=g7EPhNEOVVE')

        if any(elem in message.content.lower() for elem in ['can you', 'do this', 'but can']):
            await channel.send('https://youtu.be/v8eIuhPstno?list=PLYH8WvNV1YEnblnazwa6y27kkeqg35dfz&t=255')
        
    #     await self.client.process_commands(message) # отправляется дважды сообщение

        
def setup(client):
    client.add_cog(RandomStuff(client))