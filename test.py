 #section - 1

num = int(input("enter number:"))

if num % 2 == 0:
    print("even number")

else :
    print("odd number")



num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
num_3 = int(input("enter third number:"))

if (num_1>=num_2) and (num_1>=num_3):
 
     print(f"largest number is {num_1}")

elif (num_2>=num_1) and (num_2>=num_3):
    print(f"largest number is {num_2}")

else :
     print(f"largest number is {num_3}")

for i in range(1,51):
    print(i)



#section - 2

num = int(input("enter number:"))
i = 1
while i<=10:
    print(f"{num} product {i} = {num*i}")
     
    i = i+1

n = int(input("enter number:"))

total_sum = 0

for i in range(1,n + 1):
    total_sum = total_sum+i
print(f"the sum of first natural number is : {total_sum}")

#section - 4

number_1 = float(input("enter first number: "))
number_2 = float(input("enter second number: " ))
number_3 = float(input("enter third number: "))

print(f"sum of input is: {number_1+number_2+number_3}")

avg = (number_3+number_2+number_1)

print(f"average of input is: {avg}")


text = "hello world"
print(text.count(""))


