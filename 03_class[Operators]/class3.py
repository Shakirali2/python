a : int = 7
b : int = 2

print(a + b) # addition
print(a - b) # substration
print(a * b) # multiplication
print(a / b) # division



a : int = 11
b : int = 3

print(a % b)

print(2**2)
print(2**3)


print(12 / 3)
print(12 // 3)

print(14.8 / 3)
print(14.8 // 3)

# = Assign
a : int = 7
print(a)
a = a + 2
print(a)

a : int = 7
print(a)
a += 2
print(a)

a : int = 7
b : int = 7

print( a == b )
# a == b
# 7 == 7
# True

a : int = 7
b : str = '7'

print( a == b )

a : int = 7
b : int = 7
print( a != b )

a : int = 7
b : int = 8
print( a > b )

a : int = 7
b : int = 7
print( a > b )

a : int = 7
b : int = 8
print( a < b )

a : int = 7
b : int = 8
print( a >= b )

a : int = 7
b : int = 8
print( a <= b )

chr(65)
ord('A')

print(True and True and True and True)
print(True and True and True and False)

print(False or False or False or True)
print(False or False or False or False)

print(not True)
print(not False)

name : str = "Shakir"
print(not name=="Shakir")

x : str = 'abc'
z : str = 'abc'

print(id(x))
print(id(z))

x is z

x is not z

name : list[str] = [chr(i) for i in range(65,91)]
print(name)

for i in range(len(name)):
    print(i)
    if name[i] =="D":
        print("True")
        break
print("D" in name)
print("D" not in name)
print("Pakistan" in name)

names : list[str] = ['sir Zia','Sir Inam', 'Qasim']
uinput : str = input("Enter your name")
print(uinput in names)
print(uinput not in names) 
name : list[str] = [chr(i) for i in range(65,91)]
print(name)

for i in range(len(name)):
    print(i)
    if name[i] =="D":
        print("True")
        break
print("D" in name)

data = ('qasim', 7, 3.2)
print(data[0],data[1], data[2])
print(*data)

print("a"*3)
