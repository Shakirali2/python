def obj1_speak():pass
def obj2_speak():pass

obj1_name : str = "Sir Zia"
obj2_name : str = "Muhammad Qasim"

# OOP (Object Oriented Programming)
# *class
#     * method
#         * first argument must be additional variable (self, this, or anything else)
#     * attribute
#        * connect with indivisual object
#     * class variables
#     * constructor
#         * def ```__init__(self, arg1,arg2)```
#     * class variable
#        * this value use for all objects
#            * ClassName.class_variable
# ```
# class ClassName():
#       class_variable1 : type = Value   
# ```

# ## Syntax of class
# ```
# class ClassName():
#     pass
# ```

class Teacher():
    def __init__(self, teacher_id : int, teacher_name : str) -> None:  # method/constructor
        self.name : str = teacher_name # self.attribute_name = value
        self.teacher_id : int = teacher_id
        self.organization_name : str = "PIAIC"


    def speak(self, words: str) -> None: # method
        print("f{self.name} is speaking {words}")

    def teaching(self, subject : str) -> None: # method
        print(f"{self.name} is teaching {subject}...!")

obj1: Teacher = Teacher(1,"Sir Zia Khan") # initialize object->calling constructor method only this time 
# obj1 = object, teacher class instance


obj2 : Teacher = Teacher(2, "Muhammad Qasim")
obj3: Teacher = Teacher(3, "Sir Inam")

print(obj1_name)
print(obj1.teacher_id)
print(obj1.organization_name)
print(obj1.teaching("Generative AI"))


print(obj2.name)
print(obj2.teacher_id)
print(obj2.organization_name)
print(obj2.teaching("Deep Learning"))

print(obj3.name)
print(obj3.teacher_id)
print(obj3.organization_name)
print(obj3.teaching("Web Development"))

#########
#* class variable
#* this value use for all objects
#    * ClassName.class_variable
#    * object_name.class_variable
# ```
# class ClassName():
#       class_variable1 : type = Value  


class Teacher():
    counter : int = 0
    help_line_number : str  = "03462675919" # class variable2

    def __init__(self, teacher_id : int, teacher_name : str) -> None:  # method/constructor
        self.name : str = teacher_name # self.attribute_name = value
        self.teacher_id : int = teacher_id
        self.organization_name : str = "PIAIC"
        Teacher.counter += 1

    def speak(self, words: str) -> None: # method
        print("f{self.name} is speaking {words}")

    def teaching(self, subject : str) -> None: # method
        print(f"{self.name} is teaching {subject}...!")

        def details(self)-> None:
            information : str = f"""
Teacher name is {self.name}
our help line number is {Teacher.help_line_number}
"""
            print(information)


obj1: Teacher = Teacher(1,"Sir Zia Khan")
obj2 : Teacher = Teacher(2, "Muhammad Qasim")

print(Teacher.counter, obj1.counter)
print(obj1.counter)
print(obj2.counter)
print(Teacher.counter)

print(obj1.help_line_number)
print(obj2.help_line_number)
print(Teacher.help_line_number)
#################

# 1. Inheritance
# class ChiledClass(ParentClass):
#       pass

class Parents():
    def __init__(self)->None:
        self.eye_color : str = "Brown"
        self.hair_color : str = "Black"

    def speak(self, words : str) ->None:
        print(f"Parent method speak : {words}")

    def watching(self, object_name : str) ->None:
        print(f"You are looking {object_name}")

class Child(Parents):
    def teaching(self, subject : str = None)-> None:
        print(f"Child method for teaching : {subject}")

obj1 : Parents = Parents()
print(obj1.eye_color)
print(obj1.hair_color)
obj1.speak("Pakistan Zindabad")
obj1.watching("TV")

print("=======Child object=======")
## Child Object


obj2 : Child = Child()
(obj2.watching("Cenima"))
(obj2.speak("Hello World"))
print(obj2.eye_color)
print(obj2.hair_color)
obj2.teaching("Generative AI")

######

class Employee():
    def __init__(self, name: str) -> None:
        self.name : str = name
        self.education : str = ""
        self.department : str = ""

class Designer(Employee):
    def __init__(self, title:str, name : str) -> None:
        super().__init__(name)
        self.title : str = title
        
class Developer(Employee):
    def __init__(self, title:str, name : str) -> None:
        super().__init__(name)
        self.title : str = title
        self.programming_skils : list[str] = ["python"]



designer1 : Designer = Designer("Animation Artist", "Asif Khan")
 
dev1 : Developer = Developer("GenAI Engineer", "Hamza")

print(designer1.title)
print(dev1.programming_skils)












