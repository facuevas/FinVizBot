import discord
from finviz_screener import *
from settings import *

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.content.startswith('!jb'):
            channel = message.channel
            await channel.send("```{0}```".format(display_table()))

client = MyClient()
client.run(DISCORD_API_KEY)