class rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width

x = rectangle(10,6)

ar = x.length * x.width
print("Area of rectangle =", ar)
    