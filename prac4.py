n = int(input("Enter number of students: "))
marks = []
names =[]
i = 0
while i<n:
    name = input("enter student name: ")
    mark = float(input("enter student marks: "))


    names.append(name)
    marks.append(mark)
    i = i + 1

for i in range(n):
    if marks[i]>=60:
        continue
    else:
        print(f"students who needs help : name -- {names[i]}, marks -- {marks[i]}")

    
a = 0
b = 0
c = 0
d = 0
e = 0

for i in range(n):
    if marks[i]>=80:
        a+=1
    elif marks[i]>=70:
        b+=1
    elif marks[i]>=60:
        c+=1
    elif marks[i]>=50:
        d+=1
    else:
        e+=1

print(f"No. of students got grade A : {a}") 
print(f"No. of students got grade B : {b}")
print(f"No. of students got grade C : {c}")   
print(f"No. of students got grade D : {d}")
print(f"No. of students got grade E : {e}")  