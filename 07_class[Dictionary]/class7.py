# list

data : list[str] = ["Muhammad Aslam", "Muhammad Qasim", "MSDS"]

# Dictionary
# * Key:value (item)
#    * key replacement of indexes
#    * value item
#    * dic_variable[key]
#       *dict_variable[new_key] = new_key
#           *add new value
#           * update value




from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[str,str] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        "abc" : [1,2,3],
                        "xyz" : {1,2,3},
                        'efg' : (1,2,3)
                        'cde' : {"a":1, "b":2}
                        100: "Pakistan",
                        # [1,2,3] : "Pakistan" # error
                        # (1,2,3) : "Pakistan" # error
                        }

print(data)
pprint.pprint(data)
print(data["name"])
print(data['fname'])
print(data['education'])
# print(data[0]) # index = key
princt(data['cde']['b'])


# set data type
data : set = {7,1,2,1,1,1,1,3,2}
print(data) # return unique 
print(data[0]) # error occur

[i for i in dir(data) if "__" not in i] # Values chack for DataSet


abc : set = {1,2,3,2,2,2,1}
print(abc)
xyz : list[int] = list(abc)
print(xyz)


from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : dict[Key, Value] = {}

data['name'] = "Muhammad Qasim" # add new key and values
data['fname'] = "Muhammad Aslam"
data['education'] = "MSDS"

print(data)


########

from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[str,str] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print(data)

data['name'] = "M.Qasim" # update
print(data)

[i for i in dir(data) if "__" not in i] # Values chack for Dictionary


from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[str,str] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }
#                  Key
print(data.get('pakistan',"NA")) # not generate error
print(data.get('name',"NA"))

print(data.keys()) # keys
print(data.values()) # values
print(data.items()) #

#####
for k in data.keys():
    print(k, data[k])
[k for k in data.keys] # comprehensive style

######
for v in data.values():
    print(v)
[v for v in data.values]

#####
for k,v in data.items():
    print(k,v)

# comprehensive style
{k:v for k,v in data.items()}
{v:k for k,v in data.items()}

#  Shuffle
a : int = 7
b : int = 9

a, b = b, a # Shuffle
print(a,b)

####
keys : list[str] = ['id', 'name', 'fname', 'course']

data : dict[Key,Value] = {}

print(data)

data.fromkeys(keys) # inline
data = data.fromkeys(keys) # inline
print(data)


 














