import discord
import Storage
import io
from PIL import Image, ImageDraw, ImageFont
import Pillow

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
    
    if contents.startswith("!help"):
      print("8")
      await message.channel.send(Storage.defaultReply)
    
    if contents.startswith("!templates"):
      for template in Storage.Templates:
        await message.channel.send(template)

    if contents.startswith("!choose"):
      Storage.memedict[user] = Storage.meme(user)
      if user not in Storage.memeStorage:
        Storage.memeStorage[user] = []
    # Extract the template name from the command
      template_name = contents[8:]  
      if template_name in Storage.Templates:
        # Retrieve the file path for the template name
        file_path = Storage.Templates[template_name]
        with open(file_path, 'rb') as picture:
          Storage.memedict[user].image_data = picture.read()
          Storage.memedict[user].image = Image.open(io.BytesIO(Storage.memedict[user].image_data))
          Storage.memedict[user].Printvalues()
        print("got the picture")
        await message.channel.send("Send the upper text to the meme. following '!textup'.")
      else:
        await message.channel.send(f"template name '{template_name}' not found")
      

    if contents.startswith("!image"):
      Storage.memedict[user] = Storage.meme(user)
      if user not in Storage.memeStorage:
        Storage.memeStorage[user] = []
      if len(attachments) <= 0:
        await message.channel.send("Attach a picture after '!image' and then type 'text'")
      else:
        picture = attachments[0]
        filename = picture.filename
        print(filename)
      # check if the file that is attached is an image(we use funktion lower() to make sure that like PNG also gets through)
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
          Storage.memedict[user].image_data = await picture.read()
          Storage.memedict[user].image = Image.open(io.BytesIO(Storage.memedict[user].image_data))
          Storage.memedict[user].Printvalues()
          print("got the picture")
          await message.channel.send("Send the upper text to the meme. following '!textup'.")
        else:
          await message.channel.send("Attach a picture after '!image'")

    if contents.startswith("!textup"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 0:
          con = contents[7:]
          Storage.memedict[user].textup = con
          if len(con) <= 20:
            Storage.memedict[user].i += 1
            await message.channel.send("Send the bottom text to the meme, following '!textdown'.")
          else: 
            await message.channel.send("The max characters for textup is 20")
        else:
          await message.channel.send("Use command '!make a meme' to make your own meme!!!")

    if contents.startswith("!textdown"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 1:
          con = contents[10:]
          print(con)
          Storage.memedict[user].textdown = con
          if len(con) <= 20: 
            Storage.memedict[user].i += 1
            await message.channel.send("You can now request the meme by using '!meme'")
          else:
            await message.channel.send("The max characters for textdown is 20")
        else:
          print("5")
          await message.channel.send(Storage.defaultReply)


    if contents.startswith("!meme"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 2:
          await Pillow.meme(message, user)
          del Storage.memedict[user]
        else:
          print("6")
          await message.channel.send(Storage.defaultReply)
      else:
        print("7")
        await message.channel.send(Storage.defaultReply)
    
    if contents.startswith("!Print my memes"):
      await Pillow.send_user_memes(message, user)
               
token = get_token()
client.run(token)

# !make a meme
# Bot: !image efterfulgt med billede 
#!image (.jpg/.png)
#!textup for upper text 
#!textdown for down text
#Bot: MEME SENT .jpg/png