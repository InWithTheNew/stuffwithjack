from .animal import Animal

class Cat(Animal):
    
    def __init__(self, name):
        self.name = name
        self.species = "cat"

    def speak(self):
        return f"{self.name} says Meow!"
    
