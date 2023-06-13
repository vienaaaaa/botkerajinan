import discord
from discord.ext import commands
import random,os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)

@bot.event
async def on_ready():
    print("bot is ready")


@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.listdir("kerajinan"))
    with open(f'kerajinan/{img_name}', 'rb') as gambar:
        picture = discord.File(gambar)
    await ctx.send(file = picture)

bot.run('')















