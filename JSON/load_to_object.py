from types import SimpleNamespace
import json

header = {
    'size': 1 * 1024 * 1024,
    'content': {
        'md5': 'md5',
        'sha1': 'sha1',
        'sha256': 'sha256',
    }
}

# serialize
json_header = json.dumps(header)
assert type(json_header) is str, print('JSON Header is not a string')

# deserialize
header = json.loads(json_header, object_hook=lambda kwargs: SimpleNamespace(**kwargs))
print(header.size)
print(header.content.md5)
print(header.content.sha1)
print(header.content.sha256)

# load to custom object
from dataclasses import dataclass


@dataclass
class Item:
    t: str
    name: str

@dataclass
class CustomObject:
    name: str
    age: int
    items: [Item]

custom_obj_dict = {
    'name': 'Brent Jeffson Florendo',
    'age': 22,
    'items': [
        {
            'type': 'Device',
            'name': 'Acer Laptop'
        },
        {
            'type': 'Smartphone',
            'name': 'Acer Laptop'
        },
    ]
}


# serialize 
json_string = json.dumps(custom_obj_dict)
# deserialize
custom_obj = json.loads(json_string, object_hook=lambda kwargs: SimpleNamespace(**kwargs))
print(custom_obj.name)
print(custom_obj.age)
print(custom_obj.items)
print(type(custom_obj))
print(CustomObject(
    name=custom_obj.name,
    age=custom_obj.age,
    items=[Item(i.type, i.name) for i in custom_obj.items]
))

