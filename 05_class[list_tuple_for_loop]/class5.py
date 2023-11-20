# List
#  * iteration operation with loop
#  * apply any operation on element
 

 names: list(ste) = ['sir zia', 'Muhammad Qasim', 'Dr Noman']

 for name in names:
    print(name)
else:
    print("Hello World")

# ###
i:int = 0 # counter = 0

while i<len(names): # names lenth =3
    print(names[i])
    i += 1


 names: list(ste) = ['sir zia', 'Muhammad Qasim', 'Dr Noman']
for name in names:
    print(f'Welcome Dear Teacher {name.title()}')
    print("PIAIC Gen AI TeamZ\n")
print("Pakistan Zindabad")


input_user : str = input("Enter user name")
print(input_user)

  
data_base : list[tuple[str,str]] = [("qasim", '123'),
                                    ("sirzia", '345')
                                    ("ikhlas", '789')]
input_user : str = input("Enter user name")
input_password : str = input("Enter user password")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print("Valid User")
        break
else:
    print("Not found or Invalid user name")


magicians: list[str] = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone, that was a great magic show!") # message for everyone


#  Numbers with loop
# * range(start, end, step)

list(range(10)) # starting=0, ending = n-1

list(range(2,10)) # starting=0, ending = n-1

list(range(2,21,2))  # starting=0, ending = n-1 21-1=20, step

for n in range(2,21,2):
    print(n)

for n in range(1,11):
    print(f"{2} X {n} = {n*2}")

for n in range(1,11):
    print(f"{3} X {n} = {n*3}")

magicians: list[str] = ['alice', 'david', 'carolina']

list(enumerate(magicians))

magicians: list[str] = ['alice', 'david', 'carolina']

for index, name in enumerate(magicians):
    print(index, name)


squares: list[lnt] = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#  List comprehensive
#  for item in items_list:
#      loop_body

#  Comprehensive Style
#   [loop_body for item in items_list]

for i in range(1,11):
    print(i**2)

[i**2 for i in range(1,11)] 


digits: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

my_food = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:] # deep copy

print(my_food)
print(friend_foods)

friend_foods[0] = "Tikka"

print(my_food)
print(friend_foods)

# Tuples
names: tuple[str] = ('A', 'B', 'C')
print(names[0])
print(names[0:2])

from typing import any
data : tuple[any] = ("A",[1,2,3], True)
print(data)

data : tuple[any] = ("A",[1,2,3], True)

print(data[1])
data[1].append(20)
print(data)
