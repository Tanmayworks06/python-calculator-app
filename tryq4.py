student = {
    "name" : "Alice",
    "age" : 15
}
try:
    key = input("Enter the key to access that value: ").lower()
    print(student[key])

except KeyError:
    print("Invalid input")