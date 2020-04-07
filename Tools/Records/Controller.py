from .TableRecords import TableRecords
from .AllRecords import AllRecords
import os

class Controller:
    _wd_record = None
    _records = None

    def __init__(self):
        self._records = AllRecords(os.path.dirname(os.path.abspath(__file__)) + os.sep + "records.xml")
        self._wd_record = TableRecords(levels=self._records.GetTypesRecords(), count_record=self._records.GetCountRecords())

    def Show(self):
        self._wd_record.Show()
