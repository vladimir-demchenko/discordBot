import discord
from discord.ext import commands
from discord.utils import get
import os

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    # role = discord.utils.get(ctx.author.server.roles, name = 'hey')
    role = ctx.guild.get_role(923628180269592596)
    print(ctx)
    await ctx.message.author.add_roles(role)
    await ctx.send(f'Hello, {author.mention}!')

# @bot.command()
# async def addrole(ctx, member: discord.Member):
#     print(member)
#
#     await member.add_roles(role)


bot.run("OTIzNjIxMzU3MzM2NTI2OTI4.YcSraw.L0JgSZXYGJqX3xfj9K2ieaUY96o")
