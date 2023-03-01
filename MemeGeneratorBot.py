import discord
from Class import meme
#from Class import memedict
import io
from PIL import Image

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
    
    if contents.startswith("!image"):
      print("!image")
      if len(attachments) < 0:
        await message.channel.send("Attach a picture after '!image'")
      else:
        picture = attachments[0]
        filename = picture.filename
        print(filename)
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
          image_data = await picture.read()
          image = Image.open(io.BytesIO(image_data))
          print("got the picture")
          with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            file = discord.File(fp=image_binary, filename='image.png')
            await message.channel.send(file=file)          
        else:
           await message.channel.send("Attach a picture after '!image'")

#      await message.channel.send("Use command '!make a meme' to make your own meme")
               
token = get_token()
client.run(token)

# !make a meme
# Bot: !image efterfulgt med billede 
#!image (.jpg/.png)
#!textup for upper text 
#!textdown for down text
#Bot: MEME SENT .jpg/png