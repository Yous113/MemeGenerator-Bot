

class meme:
    def __init__(self, user_id):
        self.user_id = user_id
        self.image = 0
        self.textup = ""
        self.textdown = ""
        self.i = 0
    
    def Printvalues(self):
        print (self.user_id, self.image, self.textup, self.textdown, self.i)


Templates = {
        "deadskeleton":"Templates/deadskeleton.jpg",
        "mjcry": "Templates/mjcry.jpg",
        "mrbean": "Templates/mrbean.jpg",
        "politecat": "Templates/politecat.jpg",
        "sadpepe": "Templates/sadpepe.jpg",
        "stonks": "Templates/stonks.png"}

help_message = ""


memedict = {}
memeStorage = {}
defaultReply = "Use command '!make a meme' to make your own meme"

