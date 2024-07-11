import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from models.clip import generate_image_clip
from models.dalle import generate_image_dalle
from models.biggan import generate_image_biggan
from utils.image_processing import display_image, download_image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='generate_image')
async def generate_image(ctx, *args):
    if len(args) < 1:
        await ctx.send("Please provide a text prompt for image generation.")
        return
    
    text_prompt = ' '.join(args)
    
    # Generate image using CLIP model
    image_clip = generate_image_clip(text_prompt)
    if image_clip:
        await display_image(ctx, image_clip)
        await download_image(ctx, image_clip)
    else:
        await ctx.send("Error generating image with CLIP model.")
    
    # Generate image using DALL-E model
    image_dalle = generate_image_dalle(text_prompt)
    if image_dalle:
        await display_image(ctx, image_dalle)
        await download_image(ctx, image_dalle)
    else:
        await ctx.send("Error generating image with DALL-E model.")
    
    # Generate image using BigGAN model
    image_biggan = generate_image_biggan(text_prompt)
    if image_biggan:
        await display_image(ctx, image_biggan)
        await download_image(ctx, image_biggan)
    else:
        await ctx.send("Error generating image with BigGAN model.")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)