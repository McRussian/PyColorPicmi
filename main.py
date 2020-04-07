import sys
from PyQt5.QtWidgets import QApplication
from Tools.Records.Controller import Controller

if __name__ == '__main__':

    app = QApplication(sys.argv)

    #game = GameMainWindow()
    records = Controller()
    records.Show()
    sys.exit(app.exec_())