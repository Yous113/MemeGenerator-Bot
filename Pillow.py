import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from MemeGeneratorBot import client

@client.command()
async def meme(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    meme = Image.open(self.image)
    out = meme.resize((128,128))
    textup_font = ImageFont.truetype('impact/impact.ttf', 200)
    textup_text = self.textdown
    textdown_font = ImageFont.truetype('impact/impact.ttf', 200)
    textdown_text = self.textup
    image_editable = ImageDraw.Draw(meme)
    image_editable.text((15,15), textup_text, (252, 252, 252), font=textup_font)
    image_editable.text((215,215), textdown_text, (252, 252, 252), font=textdown_font)
