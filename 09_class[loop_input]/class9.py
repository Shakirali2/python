# Loop and input from user
# while
# for
# controls
#     break
#     continue
#     pass
# input with input function
# input from console

# Loop working on iterative data types
# list
# dictionary
# tuple
# string

#  iteration on list
l1 : list[int] = [1,2,3,4,5,6]

for n in l1:
    print(n)
    print(f"current number : {n}")

########

#  iteration on tuple
l1 : tuple[int] = (1,2,3,4,5,6)

for n in l1:
    print(n)
    print(f"current number : {n}")

#########

l1 : str = "Pakistan"

for c in l1:
    print(f"current number : {c}")
#########

#  iteration perform on keys
l1 : str = "Pakistan"

for c in l1:
    print(f"current number : {c}")

######
# iteration on dictionary

l1 : dict[str,str] = {"name":"Muhammad Qasim", "fname":"Muhammad Aslam"}

for k in l1:
    print(f"dictionary key {k} and value is {l1[k]}")

########
# iteration on set
li : set[int] = {1,2,3,4,1,1,1,1}

for k in li:
    print(f"value from list of set : {k}")
########   
l1 : list[set[int]] = list({1,2,3,4,1,1,1,1})

for k in l1:
    print(f"value from list of set : {k} ")

### Input from user

# input function
#     default type = String
# sys.argv(for console input in abc.py file)
#     default type = object

name : str = input("What is your name? : \t")

print(type(name))

print(f"Welcome dear User Mr/Mess {name}!")

#######

import sys

print("line1")
print("line2")

print(type(sys.argv))

print(sys.argv) #iterative data type

#####################
names : list[str] = ['a','b','c']
fname : list[str] = ['x','y','z']
age : list[int] = [1,2,3]

list(zip(names,fname,age))

for name,fn,ag in zip(names,fname,age):
    print(f"Welcome dear{name}, s/o {fn}!")

#############
### while loop
# while logic:  #True/False
#     loop_body

flag : bool = True # flag

current_number : int = 1

while flag:
    print(f"current number is :{current_number}")
    current_number += 1

    if current_number == 10:
        break

##############

l1 : list[int] = [100,200,300]

index : int = 0

while index < len(l1):
    print(f"current index is :{index} and list value is {l1[index]}")
    index += 1

#######

data : list [dict[str,str]] = []

flag : bool = True

while flag:
    print("Write quite or exit to stop this program")
    name : str = input("Your good name? \t:")
    education: str = input("Your last education? \t:")
    
    if name in ['exit','quite','close','stop'] or education in ['exit','quite','close','stop']:
        flag=False
        break
    data.append({"name":name,
                "education": education})
print(data)

######
# Controls
    # break
    # continue
    # pass

for i in range(1,11):
    print(i)
    if i == 5:
        break

for i in range(1,11):
    print(f"2 X {i} = {i*2}")
    break

for i in range(1,11): # Creating a range from 1 to 10
    if i == 5:
        continue # Skipping the iteration when i is 5
    print(i)

# Pass

for i in range(1,100):
    pass


def abc(a: int, b:int ) -> int:
    pass

if True:
    pass
print("Pakistan")
print("Second")

#####
prompt = """If you share your name, we can personalize the messages you see.
what is your first name?"""

name = input(prompt)
print(f"\nHello, {name}!")

# Type Casting
age:int = int(input("How old are you?"))
age >= 18
print(age)


data : list[int] = [3,5,6,3,15,18]
#extract even numbers from this list

[i  for i in data if i%2==0]
[i  for i in data if i%2!=0]
############
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
##########
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
######3

data : list[int] = [1,2,3]

while data:
    n : int = data.pop()
    print(n)

#####

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
















