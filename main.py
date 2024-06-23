import discord
from discord.ext import commands
import random

TOKEN = '59bddc6b5ef6960c66ff14d08707a961f67dfbad9d607260d7048cfe51269266'

# List of jokes
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you get if you cross a snowman and a vampire? Frostbite!",
    "Why was the math book sad? Because it had too many problems."
]

# Create a bot instance with command prefix '!'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='joke')
async def tell_joke(ctx):
    joke = random.choice(jokes)
    await ctx.send(joke)

bot.run(TOKEN)
