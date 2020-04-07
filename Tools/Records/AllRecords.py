from .LevelRecord import LevelRecord
import xml.etree.ElementTree as ET


class AllRecords:
    _records_filename = None
    _records = None
    _count_record = None

    def __init__(self, filename:str):
        self._records_filename = filename
        self._records = dict()
        self._initRecords()

    def _initRecords(self):
        tree = ET.parse(self._records_filename)
        root = tree.getroot()
        count = root.find('CountRecords')
        if count is None:
            self._count_record = 10
        else:
            try:
                self._count_record = int(count.text)
            except:
                self._count_record = 10

        for level in root.find('Levels').getchildren():
            type = LevelRecord(node=level)
            self._records[type.GetNameLevel()] = type


    def GetListRecords(self, type:str)-> list:
        pass

    def GetTypesRecords(self)-> list:
        return list(self._records.keys())

    def GetCountRecords(self)-> int:
        return self._count_record