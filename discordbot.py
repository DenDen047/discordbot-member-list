import discord
from discord.ext import commands
import os
import random
import traceback


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def presentation_list(ctx):
    members = [str(m) for m in ctx.guild.members if not m.bot]
    random.shuffle(members)

    result = '\n'.join(members)
    await ctx.send(result)


bot.run(token)
