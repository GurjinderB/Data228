class Dog:

    animal_kind = "canine" # This is an attribute, not object specific,
                           # can be changed eg: Dog.animal_kind = 'cat'

    def __init__(self, name, colour): # Initialised variables
        self.name = name
        self.colour = colour

        self.animal_kind = "canine"

 
    def bark(self, name): # This is a method, self is always needed, name is an additional parameter
        return "woof " + name
    
laika = Dog("Laika", "gold")

print(laika.bark("paula"))
print(laika.animal_kind)
Dog.animal_kind = "cat"
print(laika.animal_kind)
print(laika.colour)
Dog.colour = "blue" # Will not change the colour of liaka
print(laika.colour) 
laika.colour = "green" # Will change the colour of liaka to green
print(laika.colour) 