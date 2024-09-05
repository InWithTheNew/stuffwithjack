from .animal import Animal

class Gerbil(Animal):

    def __init__(self, name):
        self.name = name
        self.species = "gerbil"

    def speak(self):
        return f"{self.name} says squeak!"
    
