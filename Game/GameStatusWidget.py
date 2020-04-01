from PyQt5.QtWidgets import QWidget, QLabel, QComboBox
from PyQt5.QtWidgets import QHBoxLayout
from Tools.Timer import Timer

class GameStatusWidget(QWidget):

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self)
        self.setParent(parent)
        self._initUI()

    def _initUI(self):
        self.setFixedHeight(40)
        self.setMinimumWidth(600)

        hbox_layout = QHBoxLayout()
        hbox_layout.addSpacing(10)

        self._lbl_statistic = QLabel(self)
        self._lbl_statistic.setFixedWidth(150)
        self._lbl_statistic.setFixedHeight(30)
        self._lbl_statistic.setText('Statistic: ')
        hbox_layout.addWidget(self._lbl_statistic)
        hbox_layout.addStretch(1)

        self._lbl_timing = Timer(self, 150, 30)
        self._lbl_timing.Start()
        hbox_layout.addWidget(self._lbl_timing)
        hbox_layout.addStretch(1)

        self._cmb_level = QComboBox(self)
        self._cmb_level.setFixedWidth(150)
        self._cmb_level.setFixedHeight(30)
        hbox_layout.addWidget(self._cmb_level)
        hbox_layout.addSpacing(10)

        self.setLayout(hbox_layout)
