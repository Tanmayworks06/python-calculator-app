class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        print("car created!")

c1 = car("BMW","black")
c2 = car("Tesla","white")

print(c1.brand)