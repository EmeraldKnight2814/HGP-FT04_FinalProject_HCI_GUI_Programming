from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtTest import QTest
from piece import Piece

class Board(QFrame):  # base the board on a QFrame widget
    updateTimerSignal = pyqtSignal(int) # signal sent when timer is updated
    clickLocationSignal = pyqtSignal(str) # signal sent when there is a new click location
    checkMoveSignal = pyqtSignal(int, int, list, int)# Signal sent when attempting to make move
    gameOver = pyqtSignal(int, int)
    playerChange = pyqtSignal(int)

    boardWidth  = 8     # board is 8 squares wide
    boardHeight = 8     # board is 8 squares tall
    timerSpeed  = 1000     # the timer updates every 1 second
    counter     = 120    # the number the counter will count down from

    p1counter = counter
    p2counter = counter

    p1score = 0
    p2score = 0

    times_reset = -1

    current_player = 1

    speed = False

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        '''initiates board'''

        self.timer = QBasicTimer()  # create a timer for the game
        self.isStarted = False      # game is not currently started

        self.boardArray = [[Piece(0,0,0), Piece(0,1,0), Piece(0,2,0), Piece(0,3,0), Piece(0,4,0), Piece(0,5,0), Piece(0,6,0)],
                           [Piece(0,0,1), Piece(0,1,1), Piece(0,2,1), Piece(0,3,1), Piece(0,4,1), Piece(0,5,1), Piece(0,6,1)],
                           [Piece(0,0,2), Piece(0,1,2), Piece(0,2,2), Piece(0,3,2), Piece(0,4,2), Piece(0,5,2), Piece(0,6,2)],
                           [Piece(0,0,3), Piece(0,1,3), Piece(0,2,3), Piece(0,3,3), Piece(0,4,3), Piece(0,5,3), Piece(0,6,3)],
                           [Piece(0,0,4), Piece(0,1,4), Piece(0,2,4), Piece(0,3,4), Piece(0,4,4), Piece(0,5,4), Piece(0,6,4)],
                           [Piece(0,0,5), Piece(0,1,5), Piece(0,2,5), Piece(0,3,5), Piece(0,4,5), Piece(0,5,5), Piece(0,6,5)],
                           [Piece(0,0,6), Piece(0,1,6), Piece(0,2,6), Piece(0,3,6), Piece(0,4,6), Piece(0,5,6), Piece(0,6,6)]]
        self.setStyleSheet("background-color: black;")
        self.printBoardArray()

    def make_connection(self, score_board):
        score_board.resetSignal.connect(self.resetGame)
        score_board.startSignal.connect(self.start)
        score_board.speedSignal.connect(self.startSpeed)

    def logic_connection(self, game_logic):
        game_logic.updateBoardSignal.connect(self.updateBoardState)


    def updateBoardState(self, boardArray, currentPlayer):
        print("Board state updating")
        self.boardArray = boardArray
        self.current_player = currentPlayer
        if(self.speed == True):
            self.timer.stop()
            self.counter = 120
            self.timer.start(self.timerSpeed, self)
        print("Board state updated")

    def printBoardArray(self):
        '''prints the boardArray in an attractive way'''
        print("Board Array:")
        print('\n'.join(['\t'.join([str(cell.getPiece()) for cell in row]) for row in self.boardArray]))

    def mousePosToColRow(self, event):
        '''convert the mouse click event to a row and column'''
        if(self.isStarted == True):
            # (x - 1/2 width) / width
            closest_x = int((event.position().x() - self.squareWidth() / 2) / self.squareWidth())
            if (closest_x >= 7):
                closest_x = 6
            # (y - 1/2 height) / height
            closest_y = int((event.position().y() - self.squareHeight() / 2) / self.squareHeight())
            if (closest_y >= 7):
                closest_y = 6

            self.tryMove(closest_x, closest_y)

    def squareWidth(self):
        '''returns the width of one square in the board'''
        return self.contentsRect().width() / self.boardWidth

    def squareHeight(self):
        '''returns the height of one square of the board'''
        return self.contentsRect().height() / self.boardHeight

    def start(self):
        '''starts game'''
        self.isStarted = True                       # set the boolean which determines if the game has started to TRUE
        self.resetGame(1)                            # reset the game
        print("start () - timer is started")

    def startSpeed(self):
        self.isStarted = True  # set the boolean which determines if the game has started to TRUE
        self.speed = True
        self.resetGame(1)  # reset the game
        self.timer.start(self.timerSpeed, self)     # start the timer with the correct speed
        print("start () - timer is started")


    def timerEvent(self, event):
        '''this event is automatically called when the timer is updated. based on the timerSpeed variable '''
        if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
            if self.current_player == 1:
                if Board.p1counter == 0:
                    print("Game over")
                    self.gameOver.emit(self.p1score, self.p2score)
                self.p1counter -= 1
                Board.p1counter -= 1
                print('timerEvent()', self.p1counter)
                self.updateTimerSignal.emit(self.p1counter)
            elif self.current_player == 2:
                if Board.p2counter == 0:
                    print("Game over")
                    self.gameOver.emit(self.p1score, self.p2score)
                self.p2counter -= 1
                Board.p2counter -= 1
                print('timerEvent()', self.p2counter)
                self.updateTimerSignal.emit(self.p2counter)
            else:
                if Board.p1counter == 0:
                    print("Game over")
                    self.gameOver.emit(self.p1score, self.p2score)
                self.p1counter -= 1
                Board.p1counter -= 1
                print('timerEvent()', self.p1counter)
                self.updateTimerSignal.emit(self.p1counter)
        else:
            super(Board, self).timerEvent(event)      # if we do not handle an event we should pass it to the super
                                                        # class for handling

    def paintEvent(self, event):
        '''paints the board and the pieces of the game'''
        painter = QPainter(self)
        self.drawBoardSquares(painter)
        self.drawPieces(painter)

    def mousePressEvent(self, event):
        '''this event is automatically called when the mouse is pressed'''
        clickLoc = "["+str(event.position().x())+","+str(event.position().y())+"]"     # the location where a mouse click was registered
        print("mousePressEvent() - "+clickLoc)

        self.mousePosToColRow(event)

        painter = QPainter(self)
        self.drawPieces(painter)
        self.update()

        self.clickLocationSignal.emit(clickLoc)

    def resetGame(self, signal):
        '''clears pieces from the board'''
        # add times reset
        print("This is reset")
        self.times_reset += signal
        # reset array to full transparent:
        for row in range(0, len(self.boardArray)):
            for col in range(0, len(self.boardArray[0])):
                self.boardArray[row][col].setPiece(0)

        self.updateLiberties()
        self.current_player = 1

        #call piece drawing function
        painter = QPainter(self)
        self.drawPieces(painter)

        self.playerChange.emit(self.current_player)

        self.update()


    def tryMove(self, newX, newY):
        print("Emitting signal")
        self.checkMoveSignal.emit(newX, newY, self.boardArray, self.current_player)

    def updateLiberties(self):
        for row in range(0, len(self.boardArray)):
            for col in range(0, len(self.boardArray[0])):
                liberties = 0
                # Top left corner
                if(row == 0 and col == 0):
                    if(self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if(self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Bottom left corner
                elif(row == 6 and col == 0):
                    if(self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Top right corner
                elif (row == 0 and col == 6):
                    if (self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Bottom right corner
                elif (row == 6 and col == 6):
                    if (self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Top row
                elif (row == 0):
                    if (self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Bottom row
                elif (row == 6):
                    if (self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Leftmost column
                elif (col == 0):
                    if (self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Rightmost column
                elif (col == 6):
                    if (self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

                # Everywhere in between
                else:
                    if (self.boardArray[col][row + 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col][row - 1].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col + 1][row].getPiece() == 0):
                        liberties += 1
                    if (self.boardArray[col - 1][row].getPiece() == 0):
                        liberties += 1
                    # add liberties to array
                    self.boardArray[row][col].setLiberties(liberties)

        self.printLiberties(self.boardArray)

    def printLiberties(self, boardArray):
        print("Liberties:")
        print('\n'.join(['\t'.join([str(cell.getLiberties()) for cell in row]) for row in boardArray]))

    def drawBoardSquares(self, painter):
        '''draw all the square on the board'''
        self.brush = QBrush(Qt.BrushStyle.SolidPattern)
        for row in range(0, Board.boardHeight):
            for col in range (0, Board.boardWidth):
                painter.save()
                colTransformation = self.squareWidth() * col
                rowTransformation = self.squareHeight() * row
                painter.translate(colTransformation, rowTransformation)
                # If outside row, make box dark brown to contrast with board and pieces
                if (col == 0 or col == 7 or row == 0 or row == 7):
                    self.brush.setColor(QColor(100, 69, 12))
                    painter.setBrush(self.brush)
                else:
                    if(col % 2 == 0):
                        if(row % 2 == 0):
                            self.brush.setColor(QColor(138, 109, 49))
                            painter.setBrush(self.brush)
                        else:
                            self.brush.setColor(QColor(191, 162, 77))
                            painter.setBrush(self.brush)
                    else:
                        if (row % 2 == 0):
                            self.brush.setColor(QColor(191, 162, 77))
                            painter.setBrush(self.brush)
                        else:
                            self.brush.setColor(QColor(138, 109, 49))
                            painter.setBrush(self.brush)

                if((row == 0 and col == 0) or (row == 0 and col == 7)):
                    painter.fillRect(col, row, self.squareWidth() - 2, self.squareHeight() + 2, painter.brush())
                if(row == 0 or row == 7):
                    painter.fillRect(col, row, self.squareWidth() + 2, self.squareHeight() - 2, painter.brush())
                elif(col == 0 or col == 7):
                    painter.fillRect(col, row, self.squareWidth() - 2, self.squareHeight() + 2, painter.brush())
                else:
                    painter.fillRect(col, row, self.squareWidth() - 2, self.squareHeight() - 2, painter.brush())

                painter.restore()

    def drawPieces(self, painter):
        '''draw the prices on the board'''

        for row in range(0, len(self.boardArray)):
            for col in range(0, len(self.boardArray[0])):
                painter.save()

                if(self.boardArray[row][col].getPiece() == 0):
                    colour = Qt.GlobalColor.transparent  # empty square could be modeled with transparent pieces
                    brush = QBrush(Qt.BrushStyle.SolidPattern)
                    brush.setColor(colour)
                elif(self.boardArray[row][col].getPiece() == 1):
                    colour = Qt.GlobalColor.black  # empty square could be modeled with transparent pieces
                    brush = QBrush(Qt.BrushStyle.SolidPattern)
                    brush.setColor(colour)
                elif (self.boardArray[row][col].getPiece() == 2):
                    colour = Qt.GlobalColor.white  # empty square could be modeled with transparent pieces
                    brush = QBrush(Qt.BrushStyle.SolidPattern)
                    brush.setColor(colour)
                else:
                    colour = Qt.GlobalColor.transparent  # empty square could be modeled with transparent pieces
                    brush = QBrush(Qt.BrushStyle.SolidPattern)
                    brush.setColor(colour)
                # set transformation so that each piece is on an intersection
                colTransformation = self.squareWidth() * col + (self.squareWidth() * .75)
                rowTransformation = self.squareHeight() * row + (self.squareHeight() * .75)
                painter.translate(colTransformation, rowTransformation)
                # set color
                painter.setBrush(brush)
                # set piece size & draw
                radius = self.squareWidth() / 4
                center = QPointF(radius, radius)
                painter.drawEllipse(center, radius, radius)
                painter.restore()
