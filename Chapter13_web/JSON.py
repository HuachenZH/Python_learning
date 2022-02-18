# =================
# an example code of freecodecamp
# =================
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
''' # inside the quotes of data, it is the syntax of JSON, it's like [ {} {} ], it means a list of two dictionaries
info = json.loads(data) # .loads: deserialize a JSON document to a Python object
print(info[1]['name'])






