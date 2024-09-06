from .animal import Animal

class Pig(Animal):

    def __init__(self, name):
        self.name = name
        self.species = "pig"

    def speak(self):
        return f"{self.name} says Oink!"
    
