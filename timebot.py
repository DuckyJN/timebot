import discord
import pytz
import datetime
import os
from dotenv import load_dotenv

client = discord.Client()

# "process.env" accesses the environment variables for the running node process. PREFIX is the environment variable you defined in your .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!duckytime'):
        formatTime = '%I:%M:%S %p %Z'
        current_time = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
        await message.channel.send("It is now " + current_time.strftime(formatTime) + " for <@160422671404761088>.")
        
client.run(TOKEN)