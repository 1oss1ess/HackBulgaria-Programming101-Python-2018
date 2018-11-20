import json
import xml.etree.ElementTree as ET


class Jsonable:
    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )

    def prepare_for_serialization(self):
        class_name = self.__class__.__name__
        dict_ = {}

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                dict_[k] = v
            elif isinstance(v, Jsonable):
                dict_[k] = v.prepare_for_serialization()
            else:
                raise ValueError('{} is not Serializable!'.format(v))

        return {'class_name': class_name, 'dict': dict_}

    def to_json(self):
        return json.dumps(self.prepare_for_serialization(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        string_class_name = json_dict['class_name']
        current_class_name = cls.__name__
        if string_class_name == current_class_name:
            return cls(json_dict)
        else:
            raise ValueError('type {} is different to type {}!'.format(string_class_name, current_class_name))

    def to_xml(self):
        return self.prepare_for_serialization()


class Panda(Jsonable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__


class Person(Jsonable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


p = Panda(name='Ivo')
# print(p.to_json())
# json_string = p.to_json()
print(p.to_xml())
# p1 = Panda.from_json(json_string)
# print(p1 == p)
# person = Person(name='Rado')
# xmlstr = ET.tostring(p, encoding='utf8', method='xml')
# # root = tree.getroot()
# print(xmlstr)


top = ET.Element('Panda')
child = ET.SubElement(top, 'name')
child.text = 'Ivo'

tree = ET.ElementTree(top)
tree.write('output.xml')
