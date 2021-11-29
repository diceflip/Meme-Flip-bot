import os
import keep_alive
import discord


from discord.ext import commands
from requests import get
import json
client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print(f"Connected to {client.user}")
   
   
#idk why this lol
@client.command()
async def fuck(ctx):
   await ctx.reply("**You, fuck off**")

#to invite the bot
@client.command()
async def invite(ctx):
    embed=discord.Embed(title="Invite Me!", url="", description="**Click to invite - https://dsc.gg/meme-flip**", color=0x00ccff)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/0d/5a/7a/0d5a7a920f011a34adf1ccea5046fb2c.gif")
    await ctx.reply(embed=embed)

#all the commands
@client.command()
async def commands(ctx):
    embed=discord.Embed(title="Bot Commands", url="", description="$meme - for a meme\n$cry - to make the bot cry\n$laugh - to make the bot laugh to death\n$rickroll - for getting rickrolled\n$fuck - Idk why ☹\n$invite - to get the invite link of the bot", color=0x11c704)
    embed.set_thumbnail(url="https://github.com/diceflip/Meme-Flip-bot/blob/main/BotLogo.png?raw=true")
    await ctx.reply(embed=embed)
 
#do it, rickroll time
@client.command()
async def rickroll(ctx):
    embed=discord.Embed(title="Get Rickrolled, lmao!", url="", description="**That's the Handsome Rick Astley**", color=0x966908)
    embed.set_image(url="https://c.tenor.com/u9XnPveDa9AAAAAM/rick-rickroll.gif")
    await ctx.reply(embed=embed)    

@client.command()
async def source(ctx):
    embed=discord.Embed(title="Meme Flip Source Code", url="", description="**Meme Flip is an open source bot, check out the code for the bot on github - https://github.com/diceflip/Meme-Flip-bot **", color=0x00ccff)
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1414990564408262661/r6YemvF9_400x400.jpg")
    await ctx.reply(embed=embed)


#cry command
@client.command()
async def cry(ctx):
    embed=discord.Embed(title="Meme Flip :", url="", description="You made me cry, you dumb", color=0xd69a00)
    embed.set_thumbnail(url="https://c.tenor.com/vM2hP3AsiP8AAAAM/%E0%A4%87%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A5%80-%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE.gif")
    await ctx.reply(embed=embed)

#laugh command  
@client.command()
async def laugh(ctx):
    embed=discord.Embed(title="Meme Flip :", url="", description="That was soo funny!", color=0xffea00)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/2d/32/e1/2d32e156fc3b1e39869e15a00b514aab.gif")
    await ctx.reply(embed=embed)

#meme command
@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)
my_secret = os.environ['Token']
keep_alive.keep_alive()
client.run(my_secret)
#store the token of your bot inside an env file
