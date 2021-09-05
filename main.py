import os

import discord
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
keep_alive()
TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()

client.run(TOKEN)