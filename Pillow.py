import discord
import io
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from MemeGeneratorBot import client
import Storage

@client.command()
async def meme(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    user_meme = Storage.memedict[user.id]
    meme = user_meme
    meme = meme.resize((230,230))
    textup_font = ImageFont.truetype('impact/impact.ttf', 200)
    textup_text = user.textup
    textdown_font = ImageFont.truetype('impact/impact.ttf', 200)
    textdown_text = user.textdown
    image_editable = ImageDraw.Draw(meme)
    image_editable.text((15,15), textup_text, (252, 252, 252), font=textup_font)
    image_editable.text((215,215), textdown_text, (252, 252, 252), font=textdown_font)
    Storage.memedict[user].i += 1 
    Storage.memedict[user].image_data = meme.image_data
    Storage.memedict[user].image = Image.open(io.BytesIO(meme.image_data))
    await ctx.send(file = discord.File(meme))
