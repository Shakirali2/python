name : str = "Shakir"
print(name)

# boundries
# 'string text', "string text", '''string text''', """String text""""
# `string text` type script

name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bechlor in Science"
age : int = 30

card : str = "PIAIC Student Card\nStudent Name: " + name +\
    "\nAge:" + str(age) + "\n"+\
        "Education: " + education
print(card)

card : str = "piaic student card\nstudent name : " + name +\
"\nAge :" + str(age)+ "\n" +\
"Education : " + education



name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bachlor in Science"
age : int = 30

card : str = """
PIAIC Student Card
Student Name : .....
Father's Name : .....
Age: .....
Education : .....
"""

print(card)

# Define multiline string """ """ ''' '''
# F-string python

name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bachlor in Science"
age : int = 30

card : str = f"""
PIAIC Student Card
Student Name : {name}
Father's Name : {fname}
Age: {age}
Education : {education}

Total {2 + 8 + 9 + 3}
"""

print(card)



name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bachlor in Science"
age : int = 30

card : str = f"""
PIAIC Student Card 
Student Name : %s
Father's Name : %s
Age: %d
Education : %s 

""" % (name, fname, age, education)

print(card)

[i for i in dir(str) if "__" not in i]


name : str ="MUhAMMad ShAkiR" 
print(name.capitalize())
print(name.lower())

a = 7
b = 8
# {} place holder
"pakistan value a = {} and value b = {}".format(a,b)


name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bachlor in Science"
age : int = 30

card : str = """
PIAIC Student Card
Student Name : {1}
Father's Name : {0}
Age: {3}
Education : {2}
""".format(fname, name, education, age)
#           0       1       2       3
print(card)

# Recommended below two f-string format
name : str = 'Shakir ali'
fname : str = "Haider ali"
education : str = "Bachlor in Science"
age : int = 30

card : str = """
PIAIC Student Card
Student Name : {a}
Father's Name : {b}
Age: {c}
Education : {d}
""".format(a=name, b=fname, c=age, d=education)

print(card)


student_code : str = """
print("My name is Shakir ali")
a:int = 7
b:int = 8
print(a + b)
"""
exec(student_code)

# Explore String methods and attributes

# pre-define global function we have used
    
    
#      * print
#      * type
#      * id
#      * dir
#      * len

a: list[str] = [i for i in dir(str) if "__" not in i]
print(a)
print(len(a))

name : str = "MuHammAd ShaKir"
# variable_name.method()
print(name)
print(name.capitalize())


name : str = "MuHammAd ShaKir"
# variable_name.method()
print(name)
print(name.casefold())


name : str = "MuHammAd ShaKir"
# variable_name.method()
print(name)
print(name.lower())

name : str = "     MuHammAd ShaKir     "

# variable_name.method()
print(name)
print(name.lstrip())

name : str = "     MuHammAd ShaKir     "

# variable_name.method()
print(name)
print(name.rstrip())

name : str = "     MuHammAd ShaKir     "

# variable_name.method()
print(name)
print(name.strip())

import re

name : str = "     MuHammAd       ShaKir     "

# variable_name.method()
print(name)

name1 : str = re.sub(' {2,100}', ' ', name).strip()
print(name1)

name : str = "Ada Lovelace"
print(name.title())
print(name.upper())
print(name.lower())

print("Name:\t\t Shakir ali")

print("Name:\nShakir ali")

print("Name:\bShakir ali")

nostarch_url:str ='https://nostarch.com'
nostarch_url.removeprefix('https://')