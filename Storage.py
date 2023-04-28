import os

TEMPLATES_FOLDER = os.path.abspath('Templates')

class meme:
    def __init__(self, user_id):
        self.user_id = user_id
        self.image = 0
        self.image_data = 0
        self.textup = ""
        self.textdown = ""
        self.i = 0
    
    def Printvalues(self):
        print (self.user_id, self.image, self.textup, self.textdown)


templates = {"1. deadskeleton":"deadskeleton.jpg","2. mjcry":"mjcry.jpg", 
             "3. mrbean":"mrbean.jpg", "4. politecat": "politecat.jpg", 
             "5. sadpepe": "sadpepe.jpg", "6. stonks": "stonks.png"}

Templates = {
        "1. deadskeleton": os.path.join(TEMPLATES_FOLDER, "deadskeleton.jpg"),
        "2. mjcry": os.path.join(TEMPLATES_FOLDER, "mjcry.jpg"),
        "3. mrbean": os.path.join(TEMPLATES_FOLDER, "mrbean.jpg"),
        "4. politecat": os.path.join(TEMPLATES_FOLDER, "politecat.jpg"),
        "5. sadpepe": os.path.join(TEMPLATES_FOLDER, "sadpepe.jpg"),
        "6. stonks": os.path.join(TEMPLATES_FOLDER, "stonks.png")}

memedict = {}
memeStorage = {}
defaultReply = "Use command '!make a meme' to make your own meme"

