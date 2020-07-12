import discord
from discord.ext import commands
import random
from discord.utils import get
import shutil
import json
import asyncio
import os
from itertools import cycle
import colorsys
from discord import Game, Embed, Color, Status, ChannelType
import datetime
import sqlite3
import math
import sys, traceback
import time
from datetime import timedelta
from collections import OrderedDict, deque, Counter


Bot = commands.Bot(command_prefix = ".")


@Bot.event
async def on_ready():
    print('Bot online!')
    

@Bot.event
async def on_command_error(ctx, error):
    pass

@Bot.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 731841556650131476:
        for guild in Bot.guilds:
            maincategory = discord.utils.get(guild.categories, id=731841356443549727)
            channel2 = await guild.create_voice_channel(name=f"Канал {member.display_name}",category = maincategory)
            await channel2.set_permissions(member,connect=True,mute_members=True,move_members=True,manage_channels=True)
            await member.move_to(channel2)
            def check(x,y,z):
                return len(channel2.members) == 0
            await Bot.wait_for('voice_state_update',check=check)
            await channel2.delete()


@Bot.command()
@commands.has_permissions( administrator = True)
async def send(ctx, member: discord.Member, *, msg):
    await ctx.message.delete()
    await member.send('{}'.format(msg))
    await ctx.send('Сообщение отправлено')


@Bot.command()
@commands.has_permissions(manage_messages =True)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}".format(msg))


token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))