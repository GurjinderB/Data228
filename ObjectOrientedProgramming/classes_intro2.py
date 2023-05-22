class Animal:

    def __init__(self):
        self.alive = True
        self.eyes = True

    def breathe(self):
        print("on breath in one out")


class Dog(Animal):
    
    def __init__(self):
        super().__init__()
        self.eyes = 2  # changed/overridden attribute for the dog subclass
                        # example of polymorphism

    def bark(self):
        print("woof")

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, number):
        if number < 10:
            self.eyes = number

    
liaka = Dog()
liaka.breathe()
print(liaka.eyes)
liaka.eyes = 1
print(liaka.eyes)