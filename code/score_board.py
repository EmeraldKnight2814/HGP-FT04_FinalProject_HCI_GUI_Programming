from PyQt6.QtWidgets import * #TODO import additional Widget classes as desired
from PyQt6.QtCore import *

class ScoreBoard(QDockWidget):
    '''# base the score_board on a QDockWidget'''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        #create a widget to hold other widgets
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        #a button that will pass the turn if clicked once and end the game if clicked twice
        self.pass_button = QPushButton("Pass")
        self.pass_button.pressed.connect(self.passTurn)
        self.start_button = QPushButton("Start")
        self.start_button.pressed.connect(self.startGame)
        self.reset_button = QPushButton("Reset")
        self.see_rules = QPushButton("See Rules")
        self.see_rules.pressed.connect(self.seeRule)

        #create two labels which will be updated by signals
        self.label_clickLocation = QLabel("Click Location: ")
        self.label_timeRemaining = QLabel("Time remaining: ")
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.label_clickLocation)
        self.mainLayout.addWidget(self.pass_button)
        self.mainLayout.addWidget(self.start_button)
        self.mainLayout.addWidget(self.see_rules)
        self.mainLayout.addWidget(self.reset_button)
        self.mainLayout.addWidget(self.label_timeRemaining)
        self.setWidget(self.mainWidget)
        self.show()

    def center(self):
        '''centers the window on the screen, you do not need to implement this method'''

    def make_connection(self, board):
        '''this handles a signal sent from the board class'''
        # when the clickLocationSignal is emitted in board the setClickLocation slot receives it
        board.clickLocationSignal.connect(self.setClickLocation)
        # when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
        board.updateTimerSignal.connect(self.setTimeRemaining)

    @pyqtSlot(str) # checks to make sure that the following slot is receiving an argument of the type 'int'
    def setClickLocation(self, clickLoc):
        '''updates the label to show the click location'''
        self.label_clickLocation.setText("Click Location:" + clickLoc)
        print('slot ' + clickLoc)

    @pyqtSlot(int)
    def setTimeRemaining(self, timeRemainng):
        '''updates the time remaining label to show the time remaining'''
        update = "Time Remaining: " + str(timeRemainng)
        self.label_timeRemaining.setText(update)
        print('slot '+update)
        # self.redraw()

    def passTurn(self):
        print("pass")

    def startGame(self):
            # TODO: Write start sequence

    def seeRule(self):
        ruleBox= QMessageBox(self)
        ruleBox.setText("How to play/rules: Go is played by two players, called Black and White. The "
                        "lines of the board have intersections wherever they cross or touch each other. "
                        "Each intersection is called a point. Intersections at the four corners and the edges of the "
                        "board are also called a point. Go is played on the points of the board, not on the squares. The "
                        "points on which any stone is put are called occupied. All other points are called "
                        "unoccupied or empty. Players take alternate turns. The player having the turn puts one of "
                        "their stones on an empty point. Sometimes, to complete a move, a player removes stones from "
                        "the board. Sometimes there are points that may not be played on a particular turn. A player may"
                        " also pass instead of playing a stone on their turn. Once a stone is placed on the board, "
                        "the stone does not move unless it is captured. A game of Go starts with an empty board and "
                        "Black plays first, unless playing with handicap. The capture rule: If a player surrounds an "
                        "opposing stone or stones by playing on all adjacent points, those opposing stone(s) "
                        "are captured and are removed from the board. Every stone or string of stones must have at "
                        "least one adjacent point that is unoccupied. This unoccupied point is called a liberty. "
                        "Adjacent stones in a string share liberties, and the stones are said to have liberties. "
                        "If there are no empty points next to a stone or a string of stones (i.e. no liberties), "
                        "the stones are removed from the board. The only exception is that a capturing stone may "
                        "have no liberty until the stones it captures are removed. ")
        ruleBox.exec()