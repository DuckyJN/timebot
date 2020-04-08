import discord
import yaml
import pytz
import datetime

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!duckytime'):
        formatTime = '%I:%M:%S %p %Z'
        current_time = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
        await message.channel.send("It is now " + current_time.strftime(formatTime) + " for <@160422671404761088>.")

# Reads the secrets file
with open("config/secrets.yaml", 'r') as stream:
    secretToken = yaml.safe_load(stream)

client.run(secretToken)