import discord
#import requests
from Class import meme
from io import BytesIO
#from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")


@client.event
async def on_message(message):
    contents = message.content
    attachments = message.attachments
    user = message.author.id 
    
       
    if contents.startswith("!make a meme"):
      reply = "Use '!image' followed by the picture"
      user = meme(user, 0, "") 
      user.Printuser()
      await message.channel.send(reply)
    
    #if contents.startswith("!image") and i == 1:
      #if attachments:
        #for attachment in attachments:
          #if attachment.filename.endswith('.jpg') or attachment.filename.endswith('.png'):
          #  response = requests.get(attachment.url)
      #await message.channel.send(reply)
           
token = get_token()
client.run(token)

# !make a meme
# Bot: !image efterfulgt med billede 
#!image (.jpg/.png)
#!textup for upper text 
#!textdown for down text
#Bot: MEME SENT .jpg/png