from PyQt6.QtCore import *

class GameLogic(QObject):
    updateBoardSignal = pyqtSignal(list, int)
    prisonerCaptured = pyqtSignal(int, int)
    territorySignal = pyqtSignal(int, int)
    playerChange = pyqtSignal(int)

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
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1
            if(arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1

        # Bottom row
        elif (newY == 6):
            # check liberties
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1

        # Leftmost Column
        elif (newX == 0):
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX + 1].getPiece() == 0):
                liberties += 1

        # Rightmost column
        elif (newX == 6):
            # check liberties
            if (arrayIn[newY + 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY - 1][newX].getPiece() == 0):
                liberties += 1
            if (arrayIn[newY][newX - 1].getPiece() == 0):
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
            if (arrayIn[newY][newX - 1].getPiece() == current_player):
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

    def checkAllyCoordinates(self, X, Y, arrayIn, current_player):
        updated_coordinates = [False, False, False, False]

        # Top Left Corner
        if (X == 0 and Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True

        # Top Right corner
        elif (X == 6 and Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True

        # Bottom Left corner
        elif (X == 0 and Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True

        # Bottom Right corner
        elif (X == 6 and Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True

        # Top Row
        elif (Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True

        # Bottom row
        elif (Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True

        # Leftmost Column
        elif (X == 0):
            # check allies
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True

        # Rightmost column
        elif (X == 6):
            # check allies
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True

        # Everywhere in between
        else:
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates[1] = True
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates[0] = True
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates[3] = True
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates[2] = True

        arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
        return arrayIn

    def attemptCapture(self, arrayIn, current_player):
        updatedArray = arrayIn
        captured_coordinates_x = []
        captured_coordinates_y = []

        #Go through whole board, checking if piece can be captured. If so, remove it from board:
        for x in range(len(arrayIn)):
            for y in range(len(arrayIn[0])):
                if self.checkCapture(x, y, updatedArray):
                    captured_coordinates_x.append(x)
                    captured_coordinates_y.append(y)

        for i in range(len(captured_coordinates_x)):
            Y = captured_coordinates_y[i]
            X = captured_coordinates_x[i]
            self.prisonerCaptured.emit(1, current_player)
            updatedArray[Y][X].setPiece(0)
            updatedArray[Y][X].setCaptured(True)

        updatedArray = self.updateLiberties(updatedArray)
        updatedArray = self.updateAllies(updatedArray)

        return updatedArray

    def updateTerritory(self, arrayIn):
        p1territory = 0
        p2territory = 0

        for x in range(len(arrayIn)):
            for y in range(len(arrayIn[0])):
                if(arrayIn[y][x].getPiece() == 1):
                    p1territory += 1
                elif(arrayIn[y][x].getPiece() == 2):
                    p2territory += 1
                else:
                    print("No owner")
        self.territorySignal.emit(p1territory, p2territory)

    # Will check if piece can be captured
    def checkCapture(self, X, Y, arrayIn):
        captured = True

        if(arrayIn[Y][X].getPiece() == 0):
            captured = False
            return captured
        else:
            if (arrayIn[Y][X].getLiberties() == 0):
                if (arrayIn[Y][X].getAllies() == 0):
                    print("No allies or liberties")
                    captured = True
                    return captured
                else:
                    # Top left corner
                    if (X == 0 and Y == 0):
                        print("x = 0, y = 0")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured

                    # Top Right corner
                    elif (X == 6 and Y == 0):
                        print("x = 6, y = 0")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Bottom Right corner
                    elif (X == 6 and Y == 6):
                        print("x = 6, y = 6")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Bottom left corner
                    elif (X == 0 and Y == 6):
                        print("x = 0, y = 6")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Leftmost column
                    elif (X == 0):
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Rightmost column
                    elif (X == 6):
                        print("x = 6")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Top row
                    elif (Y == 0):
                        print("y = 0")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    elif (Y == 6):
                        print("y = 6")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")

                    # Everywhere else
                    else:
                        print("Inside")
                        modified_array = arrayIn
                        allies = modified_array[Y][X].getAllyCoordinates()
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")
                        self.updateAllies(modified_array)
                        self.updateLiberties(modified_array)
                        if (allies[3] == True):
                            print("Right ally")
                            if(self.checkCapture(X + 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                captured = True
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                self.updateAllies(modified_array)
                                self.updateLiberties(modified_array)
                                captured = False
                                return captured
                        if (modified_array[Y][X].getPiece() == 1):
                            modified_array[Y][X].setPiece(2)
                        elif (modified_array[Y][X].getPiece() == 2):
                            modified_array[Y][X].setPiece(1)
                        else:
                            print("What? How?")


            else:
                print("Liberties more than 1")
                captured = False
                return captured

        self.updateAllies(modified_array)
        self.updateLiberties(modified_array)

        return captured

    def makeMove(self, newX, newY, arrayIn, current_player):
        print("signal recieved")
        '''tries to move a piece'''
        # check if piece is already unoccupied:
        if (arrayIn[newY][newX].getPiece() == 0):
            # Check if neighboring pieces are empty
            liberties = self.checkLiberties(arrayIn, newX, newY)
            allies = self.checkAllies(newX, newY, arrayIn, current_player)
            arrayIn = self.checkAllyCoordinates(newX, newY, arrayIn, current_player)

            print("Liberties found: " + str(liberties))
            print("Allies found: " + str(allies))

            if (liberties > 0 or allies > 0):
                if arrayIn[newY][newX].getCaptured():
                    print("Piece cannot be placed here")
                    arrayIn[newY][newX].setPiece(0)
                else:
                    arrayIn[newY][newX].setPiece(current_player)
                    arrayIn = self.updateLiberties(arrayIn)
                    arrayIn = self.updateAllies(arrayIn)

                    boardArray = self.attemptCapture(arrayIn, current_player)
                    self.updateTerritory(boardArray)

                    # switch players
                    # NOTE: I would like to change this to Match/Case, however my machine is only capable of Python 3.9 at this time.
                    if (current_player == 1):
                        current_player = 2
                        self.playerChange.emit(current_player)
                    elif (current_player == 2):
                        current_player = 1
                        self.playerChange.emit(current_player)
                    else:
                        current_player = 1
                        self.playerChange.emit(current_player)

                    self.updateBoardSignal.emit(boardArray, current_player)
            else:
                arrayIn[newY][newX].setPiece(current_player)
                if(newX == 0 and newY == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newX == 0 and newY == 6):
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newX == 6 and newY == 0):
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newX == 6 and newY == 6):
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newX == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newX == 6):
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newY == 0):
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                elif(newY == 6):
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
                else:
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)
                        self.updateTerritory(boardArray)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                        self.playerChange.emit(current_player)
                    else:
                        print("Piece cannot be placed here")
                        arrayIn[newY][newX].setPiece(0)
        else:
            print("There is already a piece at (" + str(newX) + ", " + str(newY) + ")")

    def updateLiberties(self, boardArray):
        for row in range(0, len(boardArray)):
            for col in range(0, len(boardArray[0])):
                boardArray[col][row].setLiberties(self.checkLiberties(boardArray, row, col))

        self.printLiberties(boardArray)
        return boardArray

    def updateAllies(self, boardArray):
        for row in range(0, len(boardArray)):
            for col in range(0, len(boardArray[0])):
                current_player = boardArray[col][row].getPiece()
                boardArray = self.checkAllyCoordinates(row, col, boardArray, current_player)
                boardArray[col][row].setAllies(self.checkAllies(row, col, boardArray, current_player))
        return boardArray

    def printLiberties(self, boardArray):
        print("Liberties:")
        print('\n'.join(['\t'.join([str(cell.getLiberties()) for cell in row]) for row in boardArray]))

    def updateScore(self):
        print("score")
