# Function 
# * pre-define function
#     *provided by in language
# * user-define function
#     *custom function
# * Return and Non-return function
#    * Return
#        * we can assign this function output in any variable
#    *Non-Return
#        * only run we can't assign value to bariable

## components
# * function declaration
    # * function name
    # * Parameters
    #     * Param : type
    # * return output type
# * function body
    # * any bussiness logic write here
# * function calling
    # * function(arg1,arg2)

### Syntax function

# def function_name(param1:type, param2:type,...)->Return_type: # declaration
#     function_body # body

# function_name(arg1,arg2) # calling

### Syntaxt lambda function
# * one line function
# *without name
# *only use in this line

# lambda param1,param2 : function_body


#####
# Pre-define function
# * print
# * len
# * id
# * dir
# * chr
# * ord
# * exec

# Return and None-return function
a : str = print("Pakistan") # a = "Pakistan" | None
print(a) #None

a : int = len("Pakistan") # a = 8 return
print(a) # Return

# Create simple function without any argument(default function)

def piaic()->None: # declaration
    # function body start
    print("PIAIC Generative Artificial Intelligence") # statment1
    print("Python Crash course") # statment2
    # function body end

piaic() # calling

### Required parameters function
#                     param1       param2
def add_two_numbers(num1 : int , num2 : int)->int:
    return num1 + num2

add_two_numbers(7,20) #agr1, arg2
#######

# keyword argument
def add_two_numbers(num1 : int , num2 : int)->int:
    print(f"num1 value {num1} and num2 value {num2}")
    return num1 + num2

add_two_numbers(num2=7,num1=20)


### function with optional parameters
def add_two_numbers(num1 : int , num2 : int = 0 )->int:
    print(num1,num2) 
    return num1 + num2

add_two_numbers(7)

### Syntaxt lambda function
# * one line function
# *without name
# *only use in this line

# lambda param1,param2 : function_body

a = lambda num1, num2 : num1 + num2
print(a(7,8))
#####3
data : list[int] = [1,2,3,4,5,6,7,8,9,10]

data = list(map(lambda x:x**2, data))
print(data)
#####
data : list[int] = [1,2,3,4,5,6,7,8,9,10]

data = list(filter(lambda x:x%2==0, data))
print(data) 
######

from typing import Callable

add: Callable[[int,int],int] = lambda x,y: x + y
result = add(10,20) # result will be 30
print(result)
###
## Generator Function
# * iterate on element one by one
# * stop after each iteration
# * remember old iteration value (last iterate value)
# * next iterate
#     *go forward from last iterate value
### Generator Function

from collections.abc import Iterator
def my_range(start:int, end:int, step: int=1):
    for i in range(start,end+1,step):
        yield i # Generator function

a: Iterator[int]= my_range(1,10)
print(a)
print(list(a))


print(dir(a))

###
data:list[int] = filter(lambda x:x%2==0, range(1,101))
print(next(data))
print(next(data))
######

# Pass Unlimited arguments

def abc(*nums):
    print(nums, type(nums))
    total = 0
    for n in nums:
        total += n
    
    return total

abc(1,2,3,4,5,6)
#####

def xyz(*kargs):
    print(kargs, type(kargs))
 

xyz(a=7, b=20, c=30, x=1, y=2, name="Muhammad Qasim")

###########

def my_function(a, b, *abc, **xyz):
    print(a,b, abc, xyz)

my_function(1,2,7,9,9,9, c=20, d=30, x=100)






