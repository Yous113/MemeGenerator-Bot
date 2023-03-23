import discord
import io
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import Storage

async def meme(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    print("hej")
    user_meme = Storage.memedict[user]
    meme = Image.open(io.BytesIO(user_meme.image_data))
    #meme = user_meme
    meme = meme.resize((230,230))
    textup_font = ImageFont.truetype('impact/impact.ttf', 200)
    textup_text = user_meme.textup
    textdown_font = ImageFont.truetype('impact/impact.ttf', 200)
    textdown_text = user_meme.textdown
    image_editable = ImageDraw.Draw(meme)
    image_editable.text((15,15), textup_text, (252, 252, 252), font=textup_font)
    image_editable.text((215,215), textdown_text, (252, 252, 252), font=textdown_font)
    Storage.memedict[user].i += 1 
    Storage.memedict[user].image_data = meme.getdata()
    Storage.memedict[user].image = meme
    await ctx.channel.send(file = discord.File(meme.getdata()))
