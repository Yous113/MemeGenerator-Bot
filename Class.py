class meme:
    def __init__(self, user_id):
        self.user_id = user_id
        self.image = 0
        self.image_data = 0
        self.textup = ""
        self.textdown = ""
        self.i = 1
    
    def Printvalues(self):
        print (self.user_id, self.image, self.textup, self.textdown)

memedict = {}