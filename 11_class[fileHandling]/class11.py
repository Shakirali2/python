# Mutalbe
list_a: list[int] = [1,2,3]
list_b = list_a
list_a.append(4)
print("list_b", list_b)

# Immutable
num_a:int = 5
num_b = num_a
num_a +=1
print("num_b:", num_b)


x=30
print("Before modification:", x, id(x))
x +=1
print("After modification:", x, id(x))

##### Immutable (Pass by value/copy)
a : int = 5

def abc(num1: int)->None:
    num1 = 6
    print(f"num1 value is {num1}")

    abc(a)

    print(a)
####

a : list[int] = [1,2,3,4]

def abc(num1:list[int])->None:
    num1.append(200)
    print(f"num1 value is {num1}")

abc(a)

print(a)

######

a : list[int] = [1,2,3,4]

def abc(num1:list[int])->None:
    num1 = [7]
    num1.append(200)
    print(f"num1 value is {num1}")

abc(a) 

print(a)

########
a : list[int] = [1,2,3,4]

def abc(num1:list[int])->None:
    num1 = [1,2,3,4]
    num1.append(200) #add on element
    print(f"num1 value is {num1}")

abc(a) 

print(a)
#####
a : int = 5

print(f"First Assignment of variable a value is {id(a)}")

def abc(num1:int)->None:
    print(f"\tValue start of function {num1} address {id(num1)}")
    num1 = 6 #copy now it will change update onject

    print(f"t\num1 value end of function {num1} address {id(num1)}") # change here    
    print("\End of program")

abc(a) #pass by value imutable

print(f"End of program variable value is {a} address of a {id(a)}")

#########

x : int = 7

b : int =7
-777
print(f"X value is {x}and X address {id(x)}")
print(f"X value is {b}and X address {id(b)}")

b = 200 # update then it will change address

# print(f"X value is {b} and X address {id{b}}")

########

a : list[int] = [1,2,3,4]
b : list[int] = [1,2,3,4]

print(id(a))
print(id(b))
####
a : list[str] = ['a','b']
b : list[str] = ['c','d']

print(id(a))
print(id(b))

print(a+b)

######

### Run time Error

a : int = int(input("Enter number1:\t"))
b : int = int(input("Enter number2:\t"))

print(a / b)
#####
names:list[str] = ['Sir Zia','Sir Inam', 'Muhammad Qasim']

indx :int = int(input("Enter index number:\t"))
print(names[indx])

######
data : tuple[int,int,int] = (1,2,3)
# data[0] = 2000   # Type Error
print(data[0])

# Handle Run time error
# ```
# try:
#     logic
# except (Error_class1, Error_class2) :
#     if error accured then run this block
# else:
#     if error not accured
# finally:
#     alwalys run
# ```
#######
print("logic1")
print("logic2")
try:
    print(5/0) # Error
except ZeroDivisionError:
    print("Zero Division Error!")
print("logic4")
print("logic5")
print("logic6")
#######

print("logic1")
print("logic2")
try:
    print(5/0) # Error
except ZeroDivisionError:
    pass
print("logic4")
print("logic5")
print("logic6")

##########


print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]
try:
    print(5/2) # Error
    print(l1[0])
#    print(xyz)

except (ZeroDivisionError,IndexError,NameError):
    print("Zero Division Error!")
print("logic4")
print("logic5")
print("logic6")













