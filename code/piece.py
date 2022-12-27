class Piece(object):
    NoPiece = 0
    Black = 1
    White = 2
    Status = 0 #default to nopiece
    liberties = 0 #default no liberties
    ally_count = 0 #default no allies
    x = -1
    y= -1
    captured = False
    ally_coordinates = [False, False, False, False]
                      # Above  Below  Left   Right
                      # 0      1      2      3

    def __init__(self, Piece, x, y):  #constructor
        self.Status = Piece
        self.liberties = 0
        self.ally_count = 0
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

    def setAllies(self, allies):
        self.ally_count = allies
    def getAllies(self):
        self.ally = self.ally_count
        return self.ally

    def getAllyCoordinates(self):
        self.cord = self.ally_coordinates
        return self.cord

    def setAllyCoordinates(self, coordinates):
        self.ally_coordinates = coordinates

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCaptured(self):
        cap = self.captured
        return cap

    def setCaptured(self, cap):
        self.captured = cap