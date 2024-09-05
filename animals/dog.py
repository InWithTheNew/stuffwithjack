from .animal import Animal

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.species = "dog"

    def speak(self):
        return f"{self.name} says Woof!"
    
