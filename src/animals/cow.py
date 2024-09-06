from .animal import Animal

class Cow(Animal):

    def __init__(self, name):
        self.name = name
        self.species = "Moo"

    def speak(self):
        return f"{self.name} says Moo!"
    
