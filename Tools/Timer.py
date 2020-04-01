from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5 import Qt
import datetime


class Timer(QWidget):
    _width = None
    _height = None
    _timer = None
    _lbl_text = None
    _lbl_time = None
    _hours = None
    _minutes = None
    _seconds = None

    def __init__(self, parent:QWidget = None, width:int = 120, height:int = 20):
        QWidget.__init__(self)
        self.setParent(parent)
        self._width = width
        self.setFixedWidth(self._width)
        self._height = height
        self.setFixedHeight(self._height)
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._handlerTimerSignal)
        self._initUI()

        self.show()

    def _initUI(self):
        self._lbl_text = QLabel(self)
        self._lbl_text.setGeometry(2, 2, 80, self._height - 4)
        self._lbl_text.setAlignment(Qt.Qt.AlignVCenter | Qt.Qt.AlignRight)
        self._lbl_text.setText("Time:")

        self._lbl_time = QLabel(self)
        self._lbl_time.setGeometry(85, 2, self._width - 85, self._height - 4)

    def Start(self):
        self._timer.start()
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

    def _handlerTimerSignal(self):
        self._seconds += 1
        if self._seconds == 60:
            self._minutes += 1
            if self._minutes == 60:
                self._hours += 1
                self._minutes = 0
            self._seconds = 0

        self._lbl_time.setText("{hours} : {minutes} : {seconds}".format(hours=self._hours,
                                                                        minutes=self._minutes,
                                                                        seconds=self._seconds))

    def Stop(self):
        self._timer.stop()

    def GetTimer(self)-> tuple:
        return (self._hours, self._minutes, self._seconds)