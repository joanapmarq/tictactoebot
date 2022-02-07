import discord
from gamelogic import GameLogic
from board import Board
from discord.ext import commands
from dotenv import load_dotenv

TOKEN = load_dotenv("TOKEN")
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("Ready")

@client.command()
async def tabuleiro(ctx):
    await ctx.send("hey",view=Board(ctx))


client.run(TOKEN)
