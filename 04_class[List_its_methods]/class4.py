name1 : str = "Qasim"
name2 : str = "Qasim"
name3 : str = "Qasim"

# List
# * dynamic length
# * hetrogenous data types (Multiple type)
# * Index
#     *positive 0 to n-1
#     *negative -1 to length
# Slicing 
    # * variable `names[start:end:step]`
    # * start : int = include
    # * end : int = n-1
    # * step : int = sequance


# ->        0         1          2
names = ["Qasim", "Sir Zia", "Sir Inam"]
# <-        -3        -2        -1

print(names[0])
print(names[-3])
print(names[-2])

from typing import Any
names : list[Any] = ["Qasim", "Sir Zia", "Sir Inam"]

print(f'Founder of PIAIC {names[-2]}')
print(f'Founder of Paic {names[-2].upper}')
characters : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXY")
print(characters)

wao = list('abcdef')
print(wao)

shakir = list('shakir')
print(shakir)

characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

#  default slicing go from left to right

print(characters[0:2]) # 0= include : index 2-1 = 1
print(characters[:2])  # not pass any number = all
print(characters[-26:-24]) # 0= include : index -24-1 = -25
print(characters[:2:1]) # 0= include : index 2-1 = 1
print(characters[::2])
print(characters[::-1]) # <-
print(characters[1:-3])

characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(characters[1:-3])

print(characters[-2:-5:-1])

names : list[Any] = ["Qasim", "Sir Zia", "Sir Inam", 20, True]

print(names)
names[0] = "Muhammad Qasim"
print(names[0])

# del names[3]


a : str = print("Pakistan")
print(a)

print([i for i in dir(list) if "--" not in i])

# Help
# * help(object)
# * object?
# * object??
# * ?object
# * ??object

# help(print)

# pop method
names : list[Any] = ["Qasim", "Sir Zia", "Sir Inam", 20, True]

print(names)
a : str = names.pop() #pop return method
print(a)
print(names)

#  append method add element in last

name : list[str] = []

names.append("Sir Zia") #add element in last
names.append("Sir Inam")  #add element in last
names.append("Qasim") #add element in last

print(names)

# insert
names : list[str] = ['a', 'b', 'c']
print(names)
names.insert(1,"Qasim") #insert on particular position
print(names)

# Delete
a : list [str] = [1,2,3,4,5]
del a[1:3] # remove object from memory
print(a)
 
# Clear
a : list[str] = [1,2,3]
a.clear()# remove all element but object is remain
print(a)

# Copy

a : list[str] = ['a', 'b', 'c']
b = a # Shallow copy
print(a)
print(b)

b[0] = 'pakistan' # change only b variable but both variable updated

print(a)
print(b)


a : list[str] = ['a', 'b', 'c']
b = a.copy() # Deep copy
print("a",a)
print("b",b)

b[0] = 'pakistan' # change only b variable but both variable updated

print("a",a)
print("b",b)

# Count
names : list[str] = ['a','a', 'a','b','c','c']
print(names.count("C"))
print(names.count("a"))

names : list[str] = ["Muhammad Qasim", "Sir Zia"] #GenAI founder member
new_faculty_members : list[str] = ['Sir Inam', 'Dr Noman']

names.append(new_faculty_members)
print(names)

# Extend

names : list[str] = ["Muhammad Qasim", "Sir Zia"] #GenAI founder member
new_faculty_members : list[str] = ['Sir Inam', 'Dr Noman']

names.append(new_faculty_members)
print(names)

#  =>
names : list[str] = ["Muhammad Qasim", "Sir Zia"] #GenAI founder member
new_faculty_members : list[str] = ['Sir Inam', 'Dr Noman']

names.extend(new_faculty_members)
print(names)

# Remove
names : list[str] = ['Sir Zia', 'Muhammad Qasim', 'Sir Inam', 'Dr Noman']
names.remove("Muhammad Qasim") #Remove with text value
print(names)

# Index
names : list[str] = ['Sir Zia', 'Muhammad Qasim', 'Sir Inam', 'Dr Noman']
names.index("Muhammad Qasim")
print(names)

names : list[str] = ['Sir Zia', 'Muhammad Qasim', 'Sir Inam', 'Muhammad Qasim']
names.index("Muhammad Qasim", 2) 
print(names)
# Reverse
names : list[str] = ['Sir Zia', 'Muhammad Qasim', 'Sir Inam', 'Dr Noman']
print(names)
names.reverse() # in-memory = change real data
print(names)

names : list[str] = list("ABCDEF")
print(names)
names.reverse() #in-memory = change real data
print(names)

# Sort
names : list[str] = list("ABCDEF")
names.sort() #in-memory = change real data
print(names)

names : list[str] = list("ABCDEF")
names.sort(reverse=True) #in-memory = change real data
print(names)

