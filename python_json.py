import json

# python -> json equivalents
# | Python | JSON | |
# | | dict | object |
# | list, tuple | array |
# | str | string |
# | int, long, float | number |
# | True | true |
# | False | false |
# | None | null |

# Conversion of a python dict to json string is called serialization/ encoding
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person)
# {"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
# {
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "name": "John",
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }
print(personJSON)

# Create a separate file with the json data using dump()
with open("data.json", "w") as f:
    json.dump(person, f, indent=4)

# The json.dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file.
# The json.dumps() method encodes any Python object into JSON formatted String.

# Deserialization/Decoding - Conversion of json string or json to python dict:
# Convert json string to dict using loads()
dict1 = json.loads(personJSON)
print(dict1)
# {'age': 30, 'city': 'New York', 'hasChildren': False, 'name': 'John', 'titles': ['engineer', 'programmer']}
# Notice here ^ the false has capital F i.e its python cause python has True and False

# Another example of json to python conversion
sample_json = '{"name":"Ark Cool", "age": 22, "cond": false}'
sample_dict = json. loads(sample_json)
print(sample_dict)
# {'name': 'Ark Cool', 'age': 22, 'cond': False}

# ----------------------------------------------------------------------------------------------------------------------
# Converting custom objects to json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user1 = User("Ark", 22)
print(user1.name)
# userJSON = json.dumps(user1) #TypeError: Object of type 'User' is not JSON serializable
# need custom encoders for this type of object for json conversion
def user_encoder(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, 'class_name': o.__class__.__name__}
    else:
        raise TypeError('TypeError: Object of type User is not JSON serializable')


# call the dumps again for object user1
userJSON = json.dumps(user1, default=user_encoder)
print(userJSON) # {"name": "Ark", "age": 22, "class_name": "User"}


# for conversion of json back into an object we need a custom deserializer
def user_decoder(d):
    if d['class_name'] == User.__name__:
        # return an object of class User
        return User(name=d['name'], age=d['age'])
    return d


# convert to an object
user = json.loads(userJSON, object_hook=user_decoder)
print(user) # <__main__.User object at 0x7fd4eb90c2b0>
# ----------------------------------------------------------------------------------------------------------------------
