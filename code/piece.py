# TODO: Add more functions as needed for your Pieces
class Piece(object):
    NoPiece = 0
    White = 2
    Black = 1
    Status = 0 #default to nopiece
    liberties = 0 #default no liberties
    x = -1
    y= -1

    def __init__(self, Piece,x,y):  #constructor
        self.Status = Piece
        self.liberties = 0
        self.x = x
        self.y = y

    def getPiece(self): # return PieceType
        return self.Status

    def setPiece(self, status):
        self.Status = status

    def getLiberties(self): # return Liberties
        self.libs = self.liberties
        return self.libs

    def setLiberties(self, liberties): # set Liberties
        self.liberties = liberties

    def getX(self):
        return self.x

    def getY(self):
        return self.y