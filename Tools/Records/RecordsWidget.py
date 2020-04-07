from PyQt5.QtWidgets import QWidget, QTableWidget

class RecordsWidget(QWidget):
    _name = None
    _count_record = None
    _width = None
    _height = None
    _table = None

    def __init__(self, name:str, width:int, height: int, count_record:int = 10):
        QWidget.__init__(self)
        self._name = name
        self._count_record = count_record
        self._width = width
        self._height = height

        self._initUI()

    def _initUI(self):
        self.setFixedWidth(self._width)
        self.setFixedHeight(self._height)
        self._initTable()


    def _initTable(self):
        self._table = QTableWidget(self)
        self._table.setGeometry(5, 5, self._width - 10, self._height - 10)
        self._table.setColumnCount(3)
        self._table.setRowCount(self._count_record)
        self._table.setHorizontalHeaderLabels(["Имя", "Дата", "Время"])
        self._table.setColumnWidth(0, int(self._width * 0.45))
        self._table.setColumnWidth(1, int(self._width * 0.33))
        self._table.setColumnWidth(2, int(self._width * 0.17))
