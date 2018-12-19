import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("mv!"), pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for mv!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Utkarsh')
    client.loop.create_task(status_task())
    

@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.add_field(name = 'Please Join my Server and Help and Support !! Server Link:',value ='https://discord.gg/zxBfDY7',inline = False)
      embed.add_field(name = '⚙ MODERATION COMMANDS ',value ='``m!kick``, ``m!ban``, ``m!unban``,',inline = False)
      embed.add_field(name = '😁 FUN COMMANDS ',value ='``m!virus @user<text>``, ``m!meme``,',inline = False)
      embed.add_field(name = '👥 GENERAL COMMANDS ',value ='``m!google <anything>``, ``mv!youtube <anything>``, ``m!botinvite``, ``m!ping``, ``m!serverinvite``, ``mv!avatar or mv!avatar @user``, ``m!meme``,',inline = False)
      embed.add_field(name = '⏱ EMOJI COMMANDS ',value ='``m!wow``, ``m!hi``, ``m!lol``',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      await client.say('Check your direct messages')
  	
    

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

client.run(os.getenv('Token'))
