import discord
from discord.ext import commands
import os
import traceback

client = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    activity = discord.Activity(name='YouTube', type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.idle, activity=activity)

bot.run(token)
