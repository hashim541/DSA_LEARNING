class Cookie:
    def __init__(self,color,taste):
        self.color=color
        self.taste=taste

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color
        return self.color

cookie1 = Cookie('green','sour')
print(cookie1.setColor('gen'))