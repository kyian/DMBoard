import sys
from Piece import Piece

class board:
    
    
    
    def __init__(self, x, y):
        self.height = y
        self.width= x
        self.matrix = []
        
        tmp1 = 0
        while tmp1 < y:
            tmp2 = 0
            row = []
            while tmp2 < x:
                stk = []
                row.append(stk)
                tmp2 = tmp2 + 1
                
            
            self.matrix.append(row)
            tmp1 = tmp1 + 1
     
    
    def printBoard(self):
        row = 0
        while row < self.height:
            col = 0
            while col < self.width:
                stk = self.matrix[row][col]
                if len(stk) == 0:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('o')
                    
                col = col + 1
            row = row + 1
            sys.stdout.write('\n')
    
    def addPiece(self, piece, x, y):
        self.matrix[x][y].append(piece)
        return True
        

    def getPieces(self, x,y):
        return self.matrix[x][y]
    
    def getPiece(self,x,y,z):
        return self.matrix[x][y][z]
    
    def removePiece(self, x,y,z):
        return self.matrix[x][y].pop(z)
    
    


#this is a change




if __name__ == '__main__':
    print 'what the hell'
    temp = board(2,3)
    print 'right'
    temp.printBoard()
    
    print '--------'
    tmp = Piece()
    temp.addPiece(tmp,1,1)
    temp.printBoard()
    print '--------'
    test1 = temp.getPieces(1,1)
    test1[0].printText()
    temp.printBoard()
    print '--------'
    test2 = temp.getPiece(1,1,0)
    test2.printText()
    temp.printBoard()
    print '--------'
    test3 = temp.removePiece(1,1,0)
    test3.printText()
    temp.printBoard()