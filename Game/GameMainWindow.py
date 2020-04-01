from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from Game.GameStatusWidget import GameStatusWidget
from Game.GameBoard import GameBoard


class GameMainWindow(QMainWindow):
    _status = None

    def __init__(self):
        QMainWindow.__init__(self)
        self._initUI()

    def _initUI(self):
        self.setMinimumHeight(600)
        self.setMinimumWidth(600)
        self.setWindowTitle('Game Color Picmi')

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("background-color: #c6fad8;")

        vLayout = QVBoxLayout(self.centralWidget)
        self._wd_board = GameBoard(self)
        vLayout.addWidget(self._wd_board)

        self._status = GameStatusWidget(self)
        vLayout.addWidget(self._status)

        self.show()

