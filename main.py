import os
import keep_alive
import discord
from discord.ext import commands
from requests import get
import json
client = commands.Bot(command_prefix="$")

#this is to keep the bot alive
@client.event
async def on_ready():
    print(f"Connected to {client.user}")

@client.command()
async def hi(ctx):
   await ctx.reply("hi")
@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)
my_secret = os.environ['Token']
keep_alive.keep_alive()
client.run(my_secret)
