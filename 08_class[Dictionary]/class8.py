Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key.Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }
methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

#################

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

data.clear()
print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

########################

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

del data
print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

########

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

a : str = data.pop("education")
print(a)

print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

##########

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

a : str = data.popitem("education")
print(a)

print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

############

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

a : str = data.get("Pakistan", "NA")
print(a)

print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

########

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {

                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

print("Before", data)

a : str = data.setdefault("Pakistan", "Empty value")
print(a)

print("After", data )

methods : list[str] = [m for m in dir(data) if "__" not in m]
print(methods)

##############

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        }

data1 : Dict[Key, Value] = {"name":"M.Qasim",
                            "age" : 30,
                            "Height" : "6 Feet"
                            }
data.update(data1)

print(data)


#########

import pandas as pandas
from typing import Any

students_data : Dict[str, list[Any]] ={
    "roll no": [1,2,3],
    "Name": ["Sir Zia","Sir Inam", "Muhammad Qasim"],
    "education": ["Master","Master","Master"]
}

df : pd.DataFrame = pd.DataFrame(students_data)

Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                         "fname":"Muhammad Aslam", 
                        "name":"Muhammad Qasim",
                        "education":"MSDS",
                        "name" : "M.Qasim"
                        }
print(data)

"Qasim" in """My name is Qasim, I'm working as Cheif Data Scientist!"""













































