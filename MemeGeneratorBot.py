import discord
from Class import meme
from Class import memedict
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
    
    if contents.startswith("!help"):
      await message.channel.send("Use command '!make a meme' to make your own meme")

       
    if contents.startswith("!make a meme"):
      reply = "Use '!image' followed by the picture"
      memedict[user] = meme(user)
      memedict[user].Printvalues()
      await message.channel.send(reply)
    

    if contents.startswith("!image"):
      if user in memedict:
        if memedict[user].i != 1:
          await message.channel.send("Use command '!make a meme' to make your own meme")
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
              memedict[user].i += 1 
              memedict[user].image_data = await picture.read()
              memedict[user].image = Image.open(io.BytesIO(memedict[user].image_data))
              print("got the picture")
            else:
              await message.channel.send("Attach a picture after '!image'")
      else:
        await message.channel.send("Use command '!make a meme' to make your own meme")
    
    
    if contents.startswith("!text"):
      if user in memedict:
        if memedict[user].i == 2:
          await message.channel.send ("Send the upper text to the meme. following '!textup'.")
          memedict[user].i += 1
      else:
        await message.channel.send("Use command '!make a meme' to make your own meme")
      

    if contents.startswith("!textup"):
      if user in memedict:
        if memedict[user].i == 3:
          con = contents[7:]
          memedict[user].textup = con
          memedict[user].i += 1
          await message.channel.send ("Send the bottom text to the meme, following '!textdown'.")
        else:
          await message.channel.send("Use command '!make a meme' to make your own meme")
    

    if contents.startswith("!textdown"):
      if user in memedict:
        if memedict[user].i == 4:
          con = contents[10:]
          memedict[user].textdown = con 
          memedict[user].i += 1
          await message.channel.send ("You can now request the meme by using '!meme'")
        else:
          await message.channel.send("Use command '!make a meme' to make your own meme")


    if contents.startswith("!meme"):
      if user in memedict:
        if memedict[user].i == 5:
        
        else:
          await message.channel.send("Use command '!make a meme' to make your own meme")




    



    
      







        


        
    
               
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