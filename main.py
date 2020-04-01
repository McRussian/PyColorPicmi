from Game.GameMainWindow import GameMainWindow
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)

    game = GameMainWindow()

    sys.exit(app.exec_())