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
        # Top Left Corner
        if (X == 0 and Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)


        # Top Right corner
        elif (X == 6 and Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)


        # Bottom Left corner
        elif (X == 0 and Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

        # Bottom Right corner
        elif (X == 6 and Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

        # Top Row
        elif (Y == 0):
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

        # Bottom row
        elif (Y == 6):
            # check allies
            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

        # Leftmost Column
        elif (X == 0):
            # check allies
            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)


        # Rightmost column
        elif (X == 6):
            # check allies
            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)


        # Everywhere in between
        else:
            # check allies
            if (arrayIn[Y + 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[1] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y - 1][X].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[0] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X + 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[3] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

            if (arrayIn[Y][X - 1].getPiece() == current_player):
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = True
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)
            else:
                updated_coordinates = arrayIn[Y][X].getAllyCoordinates()
                updated_coordinates[2] = False
                arrayIn[Y][X].setAllyCoordinates(updated_coordinates)

        return arrayIn

    def attemptCapture(self, arrayIn, current_player):
        updatedArray = arrayIn

        #Go through whole board, checking if piece can be captured. If so, remove it from board:
        for x in range(len(arrayIn)):
            for y in range(len(arrayIn[0])):
                if(self.checkCapture(x, y, updatedArray)):
                    updatedArray[y][x].setPiece(0)

        updatedArray = self.updateLiberties(updatedArray)
        updatedArray = self.updateAllies(updatedArray)

        return updatedArray

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
                        if(allies[3] == True and allies[1] == True):
                            print("Below and Right ally")
                            if(self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
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
                        if (allies[2] == True and allies[1] == True):
                            print("Below and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[2] == True and allies[0] == True):
                            print("Above and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[3] == True and allies[0] == True):
                            print("Above and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if(allies[3] == True and allies[1] == True and allies[0] == True):
                            print("Right, Above, and Below allies")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[0] == True):
                            print("Above and Right ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True and allies[1] == True):
                            print("Above and Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X, Y - 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[1] == True):
                            print("Below and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[2] == True and allies[1] == True and allies[0] == True):
                            print("Left, Above, and Below allies")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1,modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[0] == True):
                            print("Above and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                        if (allies[2] == True and allies[1] == True):
                            print("Below and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True and allies[1] == True):
                            print("Above and Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X, Y - 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[1] == True and allies[2] == True and allies[3] == True):
                            print("Below, right, and left ally")
                            if (self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[1] == True):
                            print("Below and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[1] == True):
                            print("Below and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[2] == True):
                            print("Left and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[3] == True and allies[2] == True and allies[0] == True):
                            print("Left, Right and Above ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[2] == True):
                            print("Left and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[0] == True):
                            print("Above and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                        if (allies[3] == True and allies[0] == True):
                            print("Above and Right ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

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
                        if (allies[3] == True and allies[2] == True and allies[1] == True and allies[0] == True):
                            print("Cardinal Allies")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y - 1, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[2] == True and allies[0] == True):
                            print("Left, Right and Above ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[1] == True and allies[0] == True):
                            print("Left, Above, and Below allies")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1,modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True and allies[2] == True and allies[3] == True):
                            print("Below, Right, and Left ally")
                            if (self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[1] == True and allies[0] == True):
                            print("Right, Above, and Below allies")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[2] == True):
                            print("Left and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True and allies[1] == True):
                            print("Above and Below ally")
                            if (self.checkCapture(X, Y + 1, modified_array) and self.checkCapture(X, Y - 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[0] == True):
                            print("Above and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                        if (allies[3] == True and allies[0] == True):
                            print("Above and Right ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True and allies[1] == True):
                            print("Below and Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array) and self.checkCapture(X, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True and allies[1] == True):
                            print("Below and Right ally")
                            if (self.checkCapture(X + 1, Y, modified_array) and self.checkCapture(X, Y + 1,modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[3] == True):
                            print("Right ally")
                            if(self.checkCapture(X + 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[2] == True):
                            print("Left ally")
                            if (self.checkCapture(X - 1, Y, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[1] == True):
                            print("Below ally")
                            if (self.checkCapture(X + 1, Y + 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured
                        if (allies[0] == True):
                            print("Above ally")
                            if (self.checkCapture(X, Y - 1, modified_array)):
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = True
                                return captured
                            else:
                                if (modified_array[Y][X].getPiece() == 1):
                                    modified_array[Y][X].setPiece(2)
                                elif (modified_array[Y][X].getPiece() == 2):
                                    modified_array[Y][X].setPiece(1)
                                else:
                                    print("What? How?")
                                captured = False
                                return captured

            else:
                print("Liberties more than 1")
                captured = False
                return captured

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
                arrayIn[newY][newX].setPiece(current_player)
                arrayIn = self.updateLiberties(arrayIn)
                arrayIn = self.updateAllies(arrayIn)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

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
                    if (self.checkCapture(newX + 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
                        boardArray = self.attemptCapture(arrayIn, current_player)

                        # switch players
                        if (current_player == 1):
                            current_player = 2
                        elif (current_player == 2):
                            current_player = 1
                        else:
                            current_player = 1

                        self.updateBoardSignal.emit(boardArray, current_player)
                    elif (self.checkCapture(newX - 1, newY, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
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
                    elif (self.checkCapture(newX, newY + 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
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
                    elif (self.checkCapture(newX, newY - 1, arrayIn)):
                        arrayIn[newY][newX].setPiece(current_player)
                        arrayIn = self.updateLiberties(arrayIn)
                        arrayIn = self.updateAllies(arrayIn)
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
