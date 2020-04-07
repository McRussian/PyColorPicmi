import xml.etree.ElementTree as ET
from .Record import Record


class LevelRecord:
    _name = None
    _ls_records = None

    def __init__(self, node: ET.Element):
        if node is None:
            self._initEmptyLevel()
        else:
            self._initLevel(node)

    def _initEmptyLevel(self):
        self._name = 'Level'
        self._ls_records = []

    def _initLevel(self, node: ET.Element):
        self._name = node.tag
        self._ls_records = []
        for node in node.findall('Record'):
            record = Record()
            record.LoadRecordFromNode(node=node)
            self._ls_records.append(record)

    def GetNameLevel(self)-> str:
        return self._name

    def GetListRecord(self)-> list:
        return self._ls_records