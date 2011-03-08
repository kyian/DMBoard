class Piece:
    def __init__(self, text):
        self.txt = text
        self.posx = -1
        self.posy = -1
        
    def __init__(self, text, x,y):
        self.txt = text
        self.posx = x
        slef.posy = y

    
    def printText(self):
        print self.txt
        
    
    def setPos(x,y):
        self.posx = x
        self.posy = y
    
    def getPos():
        return [x,y]
    
    def setText(text):
        self.txt = text
    
    def getText():
        return self.txt
    


if __name__ == '__main__':
    print 'what the hell'
    temp = Piece()
    temp.printText()