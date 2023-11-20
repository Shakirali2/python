# factorial.py

from typing import Any


class Factorial:
    def __init__(self):
        self.cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number not in self.cache:
            self.cache[number] = number * self(number - 1)
        return self.cache[number]








factorial_of = Factorial()

print(factorial_of(4))

factorial_of(5)

factorial_of(6)

print(factorial_of.cache)

#####

class StudentLogin():
    def __init__(self) -> None:
        self.__username : str = "Admin"
        self.__password : str = "Admin"

    def __dbconnectivity(self, user:str, password:str):
        print("Successfully connected")
        if user == self.__username and password == self.__password:
            return "Valid user"
        else:
            return "Invalid user"
    def update_password(self, password:str):
        self.__password = password

    def student_login(self, user: str, pass1: str):
        message : str = self.__dbconnectivity(user,pass1)
        print(message)
        
    def display_information(self):
        print(f"Hello Dear, {self.__username} and password {self.__password}")

qasim : StudentLogin = StudentLogin()

qasim.__password = 'aasd'
qasim.display_information()
qasim.student_login("qasim", "qasim123")
qasim.student_login("Admin", "Admin")
qasim.update_password("qasim123")
qasim.display_information()








