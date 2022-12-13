from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class ScoreBoard(QDockWidget):
    '''# base the score_board on a QDockWidget'''
    resetSignal = pyqtSignal(int) # Signal sent when reset button is pressed
    startSignal = pyqtSignal(int) # Signal sent when start button is pressed

    def __init__(self):
        super().__init__()
        self.initUI()

    # initiates score board UI
    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')

        #create a widget to hold other widgets
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        # a button that will pass the turn if clicked once and end the game if clicked twice
        self.pass_button = QPushButton("Pass")
        self.pass_button.pressed.connect(self.passTurn)

        # this button starts the game
        self.start_button = QPushButton("Start")
        self.start_button.pressed.connect(self.startGame)

        # this button resets the game
        self.reset_button = QPushButton("Reset")
        self.reset_button.pressed.connect(self.reset)

        # this button lets the user see the rules
        self.see_rules = QPushButton("See Rules")
        self.see_rules.pressed.connect(self.seeRule)

        # creates the labels which will be updated by signals
        self.label_clickLocation = QLabel("Click Location: ")
        self.label_timeRemaining = QLabel("Time remaining: ")
        self.label_playerTurn = QLabel("Players Turn: ")
        self.label_playerPoints = QLabel("Player Points: ")

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
        self.label_clickLocation.setText("Click Location:" + "\n" + clickLoc)
        print('slot ' + clickLoc)

    @pyqtSlot(int) # this updates the timer and shows the time remaining
    def setTimeRemaining(self, timeRemainng):
        '''updates the time remaining label to show the time remaining'''
        update = "Time Remaining: " + str(timeRemainng)
        self.label_timeRemaining.setText(update)
        print('slot '+update)
        # self.redraw()

    # this shows whose turn it is
    def setPlayersTurn(self, turn):
        '''updates the label to show the players turn'''
        self.label_playerTurn.setText("Player Turn:" + "")
        print('slot ' + '')

    # this updates the label to show the player points
    def setPlayerPoints(self, point):
        self.label_playerPoints.setText("Player Points:" + "")
        print('slot ' + '')

    # this allows the game to end if the button is clicked twice
    def passTurn(self):
        print("pass")
        # TODO: Write code to say that if the button is clicked twice it ends the game and puts up a dialog box

    # this starts the game and the timer
    def startGame(self):
        print("Start")
            # TODO: Write start sequence

    # this shows the rules and how to play the game
    def seeRule(self):
        ruleBox = QMessageBox(self)
        ruleBox.setText("How to play/rules: "
                        "\n\nGo is played by two players, called Black and White. \nThe "
                        "lines of the board have intersections wherever they cross or touch each other. "
                        "\nEach intersection is called a point. \nIntersections at the four corners and the edges of the "
                        "board are also called a point. \n\nGo is played on the points of the board, not on the squares. \nThe "
                        "points on which any stone is put are called occupied. \nAll other points are called "
                        "unoccupied or empty. \n\nPlayers take alternate turns. \nThe player having the turn puts one of "
                        "their stones on an empty point. \nSometimes, to complete a move, a player removes stones from "
                        "the board. \nSometimes there are points that may not be played on a particular turn. \nA player may"
                        " also pass instead of playing a stone on their turn. \n\nOnce a stone is placed on the board, "
                        "the stone does not move unless it is captured. \nA game of Go starts with an empty board and "
                        "Black plays first, unless playing with handicap. \n\nThe capture rule: If a player surrounds an "
                        "opposing stone or stones by playing on all adjacent points, those opposing stone(s) "
                        "are captured and are removed from the board. \n\nEvery stone or string of stones must have at "
                        "least one adjacent point that is unoccupied. \nThis unoccupied point is called a liberty. "
                        "\nAdjacent stones in a string share liberties, and the stones are said to have liberties. "
                        "\nIf there are no empty points next to a stone or a string of stones (i.e. no liberties), "
                        "the stones are removed from the board. \nThe only exception is that a capturing stone may "
                        "have no liberty until the stones it captures are removed. \n\nTypes of Capture: capture of one stone,"
                        " capture of three stones in a corner, capture of two strings, and capture by a stone with no "
                        "liberties. \n\nNo Repetition Rule: One may not play a move that repeats a previous board position."
                        " This rule prevents players from endlessly capturing and recapturing a stone, back and forth.")
        ruleBox.exec()

    # this resets the game
    def reset(self):
        print("Reset")
        self.resetSignal.emit(1)
