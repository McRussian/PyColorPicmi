from PyQt5.QtWidgets import QWidget, QTabWidget, QLabel
from Tools.Records.RecordsWidget import RecordsWidget
from PyQt5.QtCore import Qt


class TableRecords(QWidget):
    _levels = None
    _count_record = None
    _tabs = None
    _lbl_info = None
    _tables = None

    def __init__(self, levels:list, count_record:int=10):
        QWidget.__init__(self)
        self._levels = levels.copy()
        self._count_record = count_record
        self._tables = dict()

        self._initUI()

    def _initUI(self):
        self.setWindowTitle("Таблица рекордов")
        self.setFixedWidth(450)
        self.setFixedHeight(450)

        self._lbl_info = QLabel(self)
        self._lbl_info.setGeometry(10, 10, 430, 60)
        self._lbl_info.setAlignment(Qt.AlignCenter)
        self._lbl_info.setText("Поздравляю ВАС!!!\n"
                               "Вы попали в таблицу рекордов!!!")

        self._tabs = QTabWidget(self)
        self._tabs.setGeometry(10, 80, 430, 360)

        for level in self._levels:
            self._tables[level] = RecordsWidget(name=level, width=430, height=430, count_record=self._count_record)
            self._tabs.addTab(self._tables[level], level)

    def Show(self):
        self.show()