class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old!")

