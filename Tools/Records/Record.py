import xml.etree.ElementTree as ET


class Record:
    _number = None
    _name = None
    _date = None
    _time = None

    def __init__(self):
        pass

    def LoadRecordFromNode(self, node: ET.Element):
        pass

    def SaveRecordToNode(self)-> ET.Element:
        pass

