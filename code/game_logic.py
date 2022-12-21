from PyQt6.QtCore import *

class GameLogic(QObject):
    updateBoardSignal = pyqtSignal(list, int)

    created = False
    def __init__(self, parent):
        super().__init__(parent)
        created = True
    def make_connection(self, board):
        '''this handles a signal sent from the board class'''
        print("logic and board connection made")
        board.checkMoveSignal.connect(self.makeMove)

    def checkLiberties(self, arrayIn, newX, newY):
        liberties = 0
        # Top Left Corner
        if (newX == 0 and newY == 0):
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1

        # Top Right corner
        elif (newX == 6 and newY == 0):
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1

        # Bottom Left corner
        elif (newX == 0 and newY == 6):
            # check liberties
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1

        # Bottom Right corner
        elif (newX == 6 and newY == 6):
            # check liberties
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1

        # Top Row
        elif (newY == 0):
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1

        # Bottom row
        elif (newY == 6):
            # check liberties
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1

        # Leftmost Column
        elif (newX == 0):
            # check liberties
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1

        # Rightmost column
        elif (newX == 6):
            # check liberties
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1

        # Everywhere in between
        else:
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1

        return liberties

    def checkAllies(self, newX, newY, arrayIn, current_player):
        allies = 0
        # Top Left Corner
        if (newX == 0 and newY == 0):
            # check allies
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1

        # Top Right corner
        elif (newX == 6 and newY == 0):
            # check allies
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
                allies += 1

        # Bottom Left corner
        elif (newX == 0 and newY == 6):
            # check allies
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1

        # Bottom Right corner
        elif (newX == 6 and newY == 6):
            # check allies
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
                allies += 1

        # Top Row
        elif (newY == 0):
            # check allies
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
                allies += 1

        # Bottom row
        elif (newY == 6):
            # check allies
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1

        # Leftmost Column
        elif (newX == 0):
            # check allies
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1

        # Rightmost column
        elif (newX == 6):
            # check allies
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1

        # Everywhere in between
        else:
            # check allies
            if (arrayIn[newY + 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY - 1][newX].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX + 1].getPiece() == current_player):
                allies += 1
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
                allies += 1

        return allies

    def attemptCapture(self, arrayIn, current_player):
        updatedArray = arrayIn

        #Go through whole board, checking if piece can be captured. If so, remove it from board:
        for x in range(len(arrayIn)):
            for y in range(len(arrayIn[0])):
                if(self.checkCapture(x, y, updatedArray, current_player)):
                    updatedArray[y][x].setPiece(0)

        return updatedArray

    # Will check if piece can be captured
    def checkCapture(self, newX, newY, arrayIn, current_player):
        captured = True

        if(newX == 0 and newY == 0):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newX == 6 and newY == 0):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newX == 6 and newY == 6):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, -1), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newX == 0 and newY == 6):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, -1), (1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newX == 0):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (0, -1), (1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newX == 6):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (0, -1), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newY == 0):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (1, 0), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        elif(newY == 6):
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, -1), (1, 0), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False
        else:
            if (arrayIn[newY][newX].getPiece() == current_player):
                captured = False
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (arrayIn[newY + y][newX + x].getPiece() != current_player):
                    captured = False

        return captured

    def makeMove(self, newX, newY, arrayIn, current_player):
        print("signal recieved")
        '''tries to move a piece'''
        # check if piece is already unoccupied:
        if (arrayIn[newY][newX].getPiece() == 0):
            # Check if neighboring pieces are empty
            liberties = self.checkLiberties(arrayIn, newX, newY)
            allies = self.checkAllies(newX, newY, arrayIn, current_player)

            print("Liberties found: " + str(liberties))
            print("Allies found: " + str(allies))

            if (liberties > 0 or allies > 0):
                arrayIn[newY][newX].setPiece(current_player)
                arrayIn = self.updateLiberties(arrayIn)

                boardArray = self.attemptCapture(arrayIn, current_player)

                # switch players
                # NOTE: I would like to change this to Match/Case, however my machine is only capable of Python 3.9 at this time.
                if (current_player == 1):
                    current_player = 2
                elif (current_player == 2):
                    current_player = 1
                else:
                    current_player = 1

                self.updateBoardSignal.emit(boardArray, current_player)
            else:
                if(newX == 0 and newY == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newX == 0 and newY == 6):
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newX == 6 and newY == 0):
                    if (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newX == 6 and newY == 6):
                    if (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newX == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newX == 6):
                    if (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newY == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                elif(newY == 6):
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
                else:
                    if (self.checkCapture(newX + 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn, current_player)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        arrayIn = self.updateLiberties(arrayIn)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    else:
                        print("Piece cannot be placed here")
        else:
            print("There is already a piece at (" + str(newX) + ", " + str(newY) + ")")

    def updateLiberties(self, boardArray):
        for row in range(0, len(boardArray)):
            for col in range(0, len(boardArray[0])):
                liberties = 0
                # Top left corner
                if(row == 0 and col == 0):
                    if(boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if(boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Bottom left corner
                elif(row == 6 and col == 0):
                    if(boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Top right corner
                elif (row == 0 and col == 6):
                    if (boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Bottom right corner
                elif (row == 6 and col == 6):
                    if (boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Top row
                elif (row == 0):
                    if (boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Bottom row
                elif (row == 6):
                    if (boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Leftmost column
                elif (col == 0):
                    if (boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Rightmost column
                elif (col == 6):
                    if (boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

                # Everywhere in between
                else:
                    if (boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    boardArray[row][col].setLiberties(liberties)

        self.printLiberties(boardArray)
        return boardArray
    def printLiberties(self, boardArray):
        print("Liberties:")
        print('\n'.join(['\t'.join([str(cell.getLiberties()) for cell in row]) for row in boardArray]))

    def updateScore(self):
        print("score")
