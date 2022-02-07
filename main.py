import discord
from gamelogic import GameLogic
from board import Board
from discord.ext import commands

TOKEN = 'OTM4NTA5NDA3MjI0OTg3NzA5.YfrU_w.SSeyrEfLpFPwO0UcMtQ-myxYK0w'

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("Ready")

@client.command()
async def tabuleiro(ctx):
    await ctx.send("hey",view=Board(ctx))


client.run(TOKEN)
