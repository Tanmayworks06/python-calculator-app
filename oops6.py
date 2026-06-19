class animal:
    def bark(self):
        print("Animal make a sound")

class Dog(animal):
    pass

dog = Dog()
dog.bark()

# class animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(animal):
#     pass

# dog = Dog("Companion")
# print(dog.name)
# dog.speak()