class book:
    def __init__(self, name , price):
        self.name = name
        self.price = price

b1 = book("maths","$450")
b2 = book("science","$300")

print("Book name:", b1.name)
print("Price:", b1.price)

print("Book name:", b2.name)
print("Price:", b2.price)