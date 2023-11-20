print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]
try:
    print(5/2) # Error
    print(l1[0])
    # print(xyz)
    open("aa.txt")
except (ZeroDivisionError):
    print("Zero Division Error!")
except IndexError:
    print("Index Error")
except NameError:
    print("Name not defined")
except:
    print("Some thing is wrong!")
print("logic4")
print("logic5")

##############

class Studentcard():
    def __init__(self, roll_no:int, name:str, age:int) -> None:
        if age < 18 or age > 60:
            raise StudentAgeError("You are not eligible for this program!")
        self.roll_no = roll_no
        self.name = name
        self.age = age

class StudentAgeError(Exception): # custom error class
    pass

student1 = Studentcard(1,"Qasim",30)

print(student1.name, student1.roll_no, student1.age)

########

class Studentcard():
    def __init__(self, roll_no:int, name:str, age:int) -> None:
        if age < 18 or age > 60:
            raise StudentAgeError("You are not eligible for this program!")
        self.roll_no = roll_no
        self.name = name
        self.age = age

class StudentAgeError(Exception): # custom error class
    pass

student1 = Studentcard(1,"Hammad",61)

print(student1.name, student1.roll_no, student1.age)

#######
# File Handling

data = open("./abc.txt")
print(data)
[i for i in dir(data) if "__" not in i]
 
#########3
from typing import TextIO

data: TextIO = open("./abc.txt") # Connectivity with abc.txt file
print(data.read())

####
with open("./abc.txt") as file:
    print(type(file))
    print(file.read())

print("Pakistan Zindabad")


with open("./abc.txt") as file: # type: TextIO
    print(type(file))
    print(file.readline()) # read only one line (first line)
    print(file.readline())
    print(file.readline(), end="") #read only one line
    print(file.readline(), end="") # line2

    print(file.readlines()[:3]) 

##########

with open("./abc1.txt", 'r') as file: # type: TextIO
    print(file.read())
    file.write("Pakistan Zindabad")

with open("./abc1.txt", 'w') as file: # type: TextIO
    file.write("Pakistan Zindabad")

with open("./abc1.txt", 'r+') as file: # type: TextIO
    print(file.read())
    file.write("We love our country")

with open("./abc1.txt", 'r+') as file: # type: TextIO
    print(file.read())
    
    file.write("We love our country")
    file.seek(0)
    
    print("After",file.read)

## Now change modes
with open("./abc2.txt", 'w') as file: # type: TextIO
    # print(file.read())
    file.write("Pakistan")

# if file exist then it overwrite the text
# if file not exist then it will creat new file

########
with open("./abc2.txt", 'a') as file: # type: TextIO
    # print(file.read())
    file.write("Pakistan")

# if file exist then it overwrite the text
# if file not exist then it will creat new file

####
with open("./abc3.txt", 'a') as file: # type: TextIO
    # print(file.read())
    file.write("line3")

#  if file not exist then it will create new file
# add content in last
#####

with open("./abc3.txt", 'x') as file: # type: TextIO
    # print(file.read())
    file.write("line3")

#  if file not exist then it will create new file
#####

# Read some real world data file
# * image
# * csv
# * live camera


import pandas as pd

df : pd.DataFrame = pd.read_csv("./data.csv")
df : pd.DataFrame = pd.read_excel("./demo.xlsx")

print(df)
















