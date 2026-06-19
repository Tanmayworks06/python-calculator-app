nums =  [8, 15, 3, 22, 7, 11, 4] 
i = 0
while i < len(nums):
    if nums[i] > 10:
        print("first number greater than 10 is: ", nums[i])
        break
i = i + 1



for i in range(1,31):
    if i % 2 == 0:
        continue
    print(i)
    

shopping_list = [] #left

numbers = list(map(int, input("enter number: ").split())) #by help
for i in numbers:
    if i == 7:
        print("FOUND")
        break

else:
    print("NOT FOUND")


total = 0 
while True:
    nums = int(input("enter number (o to stop): "))

    if nums == 0:
        break

    if nums <0:
        continue
    total += nums

print(f"sum of positive numbers are : {total}")



