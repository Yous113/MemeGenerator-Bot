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
    meme = meme.resize((250,150))
    text_font = ImageFont.truetype('impact/impact.ttf', 25)
    textup_text = user_meme.textup
    textdown_text = user_meme.textdown
    image_editable = ImageDraw.Draw(meme)
    _, _, w1, _ = image_editable.textbbox((0, 0), textup_text, font=text_font)
    _, _, w2, _ = image_editable.textbbox((0, 0), textdown_text, font=text_font)
    image_editable.text(((250-w1)/2,5), textup_text, (250, 250, 250), font=text_font)
    image_editable.text(((250-w2)/2,115), textdown_text, (250, 250, 250), font=text_font)
    meme.save("meme.png")
    meme.close()

    Storage.memedict[user].i += 1 
    Storage.memedict[user].image = Image.open("meme.png")
    await ctx.channel.send(file = discord.File("meme.png"))
