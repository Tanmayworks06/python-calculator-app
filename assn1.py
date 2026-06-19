def greet(name):
     return f"hello {name} , welcome to python"

print(greet("tanmay"))



total = 0

for i in range(1,51):
    total += i

print("sum:" ,total)



li = ["orange", "banana", "apple", "kiwi", "jackfruit"]
li.append("mango")
li.remove("banana")
print("second fruit :" , li[1])
print("updated list : ", li)


tu = ("john", 18, "A", "new york")
w , x , y , z = tu
print("name: ", w)
print("age: ", x)
print("grade: ", y)
print("city: ", z)

print("total elements: ", len(tu))

students = {
    "alice" : 90,
    "bob" : 85,
    "clara" : 75,
    "david" : 100
    }

print("alice marks: ", students["alice"])
students["eva"] = 88
students["bob"] = 91

print("all students name and marks: ")

for name,marks in students.items():
    print(name, ":" ,marks)



set_a = {"Math", "Science", "English", "Art"} 
set_b = {"Science", "History", "English", "Music"}


a = (set_a | set_b)
print(a)
b = (set_a & set_b)
print(b)
c = (set_a - set_b)
print(c)



n = int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end="" )

    print( ) 

def print_evens(n):
    x = 2

    while x <= n:
        print(x , end=" ")
        x = x+2
print_evens(20)


def words_count(x):
    result = {}

    for word in x.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        
    return result 



print(words_count("the cat sat on the mat the cat"))


def diamonds(n):
    for i in range(1,n+1,2):
       space = " " * ((n-i) // 2)
       print(space + "*" * i)

    for i in range(n-2,0,-2):
        space = " " * ((n-i) // 2)
        print(space + "*" * i)

diamonds(5)