import discord
from discord.ext import commands
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklmnouprstuwxyzABCDEFGHIJKLMNOUPRSTUWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, I'm {bot.user}!")

@bot.command()
async def Rdpass(ctx):
    await ctx.send(gen_pass(14))

bot.run("YOUR BOT TOKEN")
