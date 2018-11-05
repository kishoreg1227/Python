import json
class JSonConverter(object):
    """Class to serialize and deserialize json"""
    __jsonString__ = None
    __jsonData__ = None
    
    def DeserializeJSonToObjects(self,jsonFile):
        with open(jsonFile) as f:
            __jsonData__ = json.load(f)
            return __jsonData__