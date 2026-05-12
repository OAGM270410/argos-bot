import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot listo: {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Soy Argos 👋")

@bot.command()
async def ping(ctx):
    await ctx.send("¡Pong! 🏓")

bot.run(os.getenv("TOKEN"))
