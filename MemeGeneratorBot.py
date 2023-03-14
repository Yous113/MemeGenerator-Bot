import discord
import Storage
import io
from PIL import Image, ImageDraw, ImageFont

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
      await message.channel.send(Storage.defaultReply)

       
    if contents.startswith("!make a meme"):
      reply = "Use '!image' followed by the picture"
      Storage.memedict[user] = Storage.meme(user)
      Storage.memedict[user].Printvalues()
      if len(Storage.memeStorage) <= 0:
        if user not in Storage.memeStorage:
          Storage.memeStorage[user] = []
      await message.channel.send(reply)
    

    if contents.startswith("!image"):
      if user in Storage.memedict:
        if Storage.memedict[user].i != 1:
          await message.channel.send(Storage.defaultReply)
        else:
          print("!image")
          if len(attachments) <= 0:
            await message.channel.send("Attach a picture after '!image' and then type 'text'")
          else:
            picture = attachments[0]
            filename = picture.filename
            print(filename)
          # check if the file that is attached is an image(we use funktion lower() to make sure that like PNG also gets through)
            if filename.lower().endswith((".jpg", ".png", ".jpeg")):
              Storage.memedict[user].i += 1 
              Storage.memedict[user].image_data = await picture.read()
              Storage.memedict[user].image = Image.open(io.BytesIO(Storage.memedict[user].image_data))
              print("got the picture")
              await message.channel.send("use command '!text'")
            else:
              await message.channel.send("Attach a picture after '!image'")
      else:
        await message.channel.send(Storage.defaultReply)
    
    
    if contents.startswith("!text"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 2:
          await message.channel.send ("Send the upper text to the meme. following '!textup'.")
          Storage.memedict[user].i += 1
        else:
          await message.channel.send(Storage.defaultReply)
      else:
        await message.channel.send(Storage.defaultReply)
      

    if contents.startswith("!textup"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 3:
          con = contents[7:]
          print(con)
          Storage.memedict[user].textup = con
          Storage.memedict[user].i += 1
          await message.channel.send ("Send the bottom text to the meme, following '!textdown'.")
        else:
          await message.channel.send(Storage.defaultReply)
      else:
        await message.channel.send(Storage.defaultReply)
    

    if contents.startswith("!textdown"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 4:
          con = contents[10:]
          print(con)
          Storage.memedict[user].textdown = con 
          Storage.memedict[user].i += 1
          await message.channel.send ("You can now request the meme by using '!meme'")
        else:
          await message.channel.send(Storage.defaultReply)


    if contents.startswith("!meme"):
      if user in Storage.memedict:
        if Storage.memedict[user].i == 5:
          with io.BytesIO() as image_binary:
            Storage.memedict[user].image.save(image_binary, 'PNG')
            image_binary.seek(0)
            file = discord.File(fp=image_binary, filename='image.png')
            Storage.memeStorage[user].append(Storage.memedict[user].image)
            await message.channel.send(file=file)  
        else:
          await message.channel.send(Storage.defaultReply)
      else:
        await message.channel.send(Storage.defaultReply)
    
    if contents.startswith("!Print my memes"):
      if len(Storage.memeStorage) <= 0:
        if user in Storage.memeStorage:
          for user, list in Storage.memeStorage:
            for meme in list:
              with io.BytesIO() as image_binary:
                meme.save(image_binary, 'PNG')
                image_binary.seek(0)
                file = discord.File(fp=image_binary, filename='image.png')
                await message.channel.send(file=file)
        else:
          await message.channel.send("You have no memes, use command '!make a meme' to make your first meme")      
      else:
        await message.channel.send("You have no memes, use command '!make a meme' to make your first meme")      
               
token = get_token()
client.run(token)

# !make a meme
# Bot: !image efterfulgt med billede 
#!image (.jpg/.png)
#!textup for upper text 
#!textdown for down text
#Bot: MEME SENT .jpg/png

#with io.BytesIO() as image_binary:
                #image.save(image_binary, 'PNG')
                #output = discord.File(fp=image_binary, filename='image.png')
                #await message.channel.send(file=output)