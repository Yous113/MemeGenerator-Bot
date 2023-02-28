import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

async def draw(ctx):
    img = Image.open('memepic.png')
    draw = ImageDraw.Draw(img)
    draw.text((0,0), 'lorum ipsum', fill=(255, 255, 255))
    img = img.save('output.png')
    display(img)