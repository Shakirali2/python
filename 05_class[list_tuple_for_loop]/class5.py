# List
#  * iteration operation with loop
#  * apply any operation on element


# Loop
names : list[str] = ['Sir Zia', "Muhammad Qasim", "Dr Noman"]
for name in names:
    print(name)

names : list[str] = ['Sir Zia', "Muhammad Qasim", "Dr Noman"]
for name in names[:2]:
    print(name)
names : list[str] = ['Sir Zia', "Muhammad Qasim", "Dr Noman"]
for name in names[::-1]:
    print(name)
for name in names:
    print(f'Welcome Dear Teacher {name.title()}')


for name in names:
    print(f'Welcome Dear Teacher {name.title()}')
    print("PIAIC Gen AI Team\n")

for name in names:
    print(f'Welcome Dear Teacher {name.title()}')
    print("PIAIC Gen AI Team\n")
print("Pakistan Zindabad\n")


cars : list[str] = ['Toyota', "Kia", "BMW"]

for car in cars:
    print(car)

data_base : list[tuple[str,str]] = [("qasim", '123'),
                           ("sirzia",'345'),
                           ("ikhlas", '789')]
for row in data_base:
    print(row)


data_base : list[tuple[str,str]] = [("qasim", '123'),
                           ("sirzia",'345'),
                           ("ikhlas", '789')]
for row in data_base:
    user, password = row
    print(user, password)

# Authentication System

data_base : list[tuple[str,str]] = [("qasim", '123'),
                           ("sirzia",'345'),
                           ("ikhlas", '789')]

input_user : str = input("Enter user name")
input_password : str = input("Ender user password")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print("Valid User")
        break
else:
    print("Not found or Invalid user name")
 
# -----------

data_base : list[tuple[str,str]] = [("qasim", '123'),
                           ("sirzia",'345'),
                           ("ikhlas", '789')]

input_user : str = input("Enter user name")
input_password : str = input("Ender user password")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print(f"Valid User {user}")
        break
else:
    print("Not found or Invalid user name")
 


familys : [str] = ["shak", "saj", "Asm", "Asf", "Nou", "Uzm"]

for family in familys :
    print(family)

