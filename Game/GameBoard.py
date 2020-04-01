from PyQt5.QtWidgets import QWidget, QGridLayout

class GameBoard(QWidget):
    _count = None

    def __init__(self, parent: QWidget = None, count: int = 15):
        QWidget.__init__(self)
        self.setParent(parent)
        self._count = count
        self._initUI()

    def _initUI(self):
        self.setMinimumHeight(550)
        self.setMinimumWidth(600)
        self.setStyleSheet("background-color: #89ae95; border: 1px solid white;")

        grid = QGridLayout(self)

        wd1 = QWidget(self)
        wd1.setFixedWidth(120)
        wd1.setFixedHeight(120)
        wd1.setStyleSheet("background-color: #895595; border: 1px solid white;")
        grid.addWidget(wd1, 0, 0)

        wd2 = QWidget(self)
        wd2.setFixedHeight(120)
        wd2.setStyleSheet("background-color: #825595; border: 1px solid white;")
        grid.addWidget(wd2, 0, 1, 1, 3)

        wd3 = QWidget(self)
        wd3.setFixedWidth(120)
        wd3.setStyleSheet("background-color: #895125; border: 1px solid white;")
        grid.addWidget(wd3, 1, 0, 3, 1)

        wd4 = QWidget(self)
        wd4.setStyleSheet("background-color: #125595; border: 1px solid white;")
        grid.addWidget(wd4, 1, 1, 3, 3)