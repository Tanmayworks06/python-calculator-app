li = [10,20,30]
try:
    x = int(input("Enter Index to access that value: "))
    print(li[x])
except IndexError:
    print("Invalid input")