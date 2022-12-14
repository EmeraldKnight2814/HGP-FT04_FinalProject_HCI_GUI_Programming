from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from board import *
from score_board import *
from game_logic import *

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # this gets the board
    def getBoard(self):
        return self.board

    # this gets the score board
    def getScoreBoard(self):
        return self.scoreBoard

    # this gets game logic
    def getGameLogic(self):
        return self.gameLogic
    def initUI(self):
        '''initiates application UI'''
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.scoreBoard)
        self.gameLogic = GameLogic()
        self.scoreBoard.make_connection(self.board)
        self.board.make_connection(self.scoreBoard)
        self.gameLogic.make_connection(self.board)

        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def center(self):
        '''centers the window on the screen'''
        gr = self.frameGeometry()
        screen = self.screen().availableGeometry().center()

        gr.moveCenter(screen)
        self.move(gr.topLeft())
        #size = self.geometry()
        #self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
