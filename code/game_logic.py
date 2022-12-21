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

    def attemptCapture(self, newX, newY, arrayIn, current_player, z):
        updatedArray = arrayIn
        print()
        print(updatedArray[newX][newY].getPiece())
        print()
        #Check which player is enemy
        if(current_player == 1):
            enemy_player = 2
        elif(current_player == 2):
            enemy_player = 1
        else:
            enemy_player = 2

        #top left corner
        if (newX == 0 and newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if(enemy_liberties == 0):
                    if(enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Top Right corner
        elif (newX == 6 and newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Bottom Left corner
        elif (newX == 0 and newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Bottom Right corner
        elif (newX == 6 and newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Top Row
        elif (newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Bottom row
        elif (newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Leftmost Column
        elif (newX == 0):
            # check allies
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Rightmost column
        elif (newX == 6):
            # check allies
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        # Everywhere in between
        else:
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            elif (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        print("Capture")
                        updatedArray[enemy_y][enemy_x].setPiece(0)
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            else:
                print("No captures")

        return updatedArray

    def checkCapture(self, newX, newY, arrayIn, current_player, z):
        updatedArray = arrayIn
        updatedArray[newY][newX].setPiece(current_player)
        capture_bool = False
        # Check which player is enemy
        if (current_player == 1):
            enemy_player = 2
        elif (current_player == 2):
            enemy_player = 1
        else:
            enemy_player = 2

        # top left corner
        if (newX == 0 and newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Top Right corner
        elif (newX == 6 and newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Bottom Left corner
        elif (newX == 0 and newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Bottom Right corner
        elif (newX == 6 and newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Top Row
        elif (newY == 0):
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Bottom row
        elif (newY == 6):
            # check allies
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Leftmost Column
        elif (newX == 0):
            # check allies
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Rightmost column
        elif (newX == 6):
            # check allies
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        # Everywhere in between
        else:
            # check allies
            if (updatedArray[newY + 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY + 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY - 1][newX].getPiece() == enemy_player):
                enemy_x = newX
                enemy_y = newY - 1
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX + 1].getPiece() == enemy_player):
                enemy_x = newX + 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")
            if (updatedArray[newY][newX - 1].getPiece() == enemy_player):
                enemy_x = newX - 1
                enemy_y = newY
                enemy_allies = self.checkAllies(enemy_x, enemy_y, updatedArray, enemy_player)
                enemy_liberties = self.checkLiberties(updatedArray, enemy_x, enemy_y)
                if (enemy_liberties == 0):
                    if (enemy_allies == (0 + z)):
                        capture_bool = True
                    else:
                        z += 1
                        updatedArray = self.checkCapture(enemy_x, enemy_y, updatedArray, current_player, z)
                else:
                    print("No captures")

        return capture_bool

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

                boardArray = self.attemptCapture(newX, newY, arrayIn, current_player, 0)

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
                if(self.checkCapture(newX, newY, arrayIn, current_player, 0)):
                    arrayIn[newY][newX].setPiece(current_player)
                    arrayIn = self.updateLiberties(arrayIn)
                    boardArray = self.attemptCapture(newX, newY, arrayIn, current_player, 0)

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
