class mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

m1 = mobile("Apple","iphone 17","$3000")
m2 = mobile("Samsung","z fold 4","$1000")

print("Brand:", m1.brand)
print("Model:", m1.model)
print("Price:", m1.price)

print("Brand:", m2.brand)
print("Model:", m2.model)
print("Price:", m2.price)