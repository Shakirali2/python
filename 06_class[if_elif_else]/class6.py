# if-else-elif
# if logic:
#     true_block
# else:
#     False_block

# Comprehensive if-else
# True_block if logic else False_block
# if
# if-else
# if-elif-else

if True:
    print("Pakistan Zindabad")
else:
    print("Hello World!")


print("Pakistan Zindabad") if True else print("Hello World!")

## Comparession operators
# ==
# >=
# <=
# !=
## logic
# and
# or
# not

if False:
    print("Pakistan Zindabad")
print("1")
print("2")

# Chain1 run only one block
if True:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

# chain2 run only one block
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif True:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")
print("pakistan")


if False:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")
print("pakistan")

# Grading Rule
from typing import Union

grade : Union[int, float] = 7.0

print(grade)
  ########

per : Union[int, float] = int(input("Enter you percentage:\t"))
# per : int | float = 88
grade : Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
######
from typing import Union
per : Union[int, float] = float(input("Enter you percentage:\t"))
# per : int | float = 88
grade : Union[str, None] = None

if (per >= 0) and (per < 33):
    grade = "Fail"
elif( per >= 33) and (per < 40 ):
    grade = "E"
elif (per >= 40) and (per < 50):
    grade = "D"
elif (per >= 50) and (per < 60):
    grade = "C"
elif (per >= 60) and (per < 70):
    grade = "B"
elif (per >= 70) and (per < 80):
    grade = "A"
elif (per >= 80) and (per <= 100):
    grade = "A+"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")

#  Student Percentages

from typing import Union
perType = Union[float, int]

percentage : list[perType] = [88, 99.9, 50, 51, 65, 70]

grades : list[str] = []

for per in percentages:
    grade : str = "Fail"
    if (per >= 0) and (per < 33):
        grade = "Fail"
    elif( per >= 33) and (per < 40 ):
        grade = "E"
    elif (per >= 40) and (per < 50):
        grade = "D"
    elif (per >= 50) and (per < 60):
        grade = "C"
    elif (per >= 60) and (per < 70):
        grade = "B"
    elif (per >= 70) and (per < 80):
        grade = "A"
    elif (per >= 80) and (per <= 100):
        grade = "A+"
    grades.append(grade)

print(percentages)
print(grades)

zip(Percentages, grades)
list(zip(percentages, grades, list(range(len(percentages)))))

roll_no : list[int] = list(range(len(percentages)))
roll_no

data_base = list(zip(roll_no,percentages,grades))
data_base

display(data_base)
sorted(data_base key=lambda x:x[1])

sorted(data_base key=lambda x:x[1], reverse=True)

cars : list[str] = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.uppor())
    else:
        print(car.title())

cars : list[str] = ['audi', 'bmw', 'subaru', 'toyota']
[i.upper() if i=='bmw' else for i in cars]

cars : list[str] = ['audi', 'bmw', 'Mehran' 'subaru', 'toyota']
for car in cars:
    if car != 'Mehran':
        print(car.upper())
    else:
        print(car.lower())

###
answer = 17
if answer != 42:
    print("That is not the correct answer, Please try again!")












