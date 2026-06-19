movies = ["animal","raavan","swarg","3idiots","murder","solo"]
print(movies[0])
print(movies[-1])
print(movies[2],movies[3])

for i in range(len(movies)):
    print(i + 1, movies[i])



numbers = []

for i in range(5):
   num = float(input(f"Enter number {i+1}: "))
   numbers.append(num)

print(numbers)

total = sum(numbers)
avg = total / len(numbers)
maxi = max(numbers)
mini = min(numbers)

print(f"sum:  {total}")
print(f"average: {avg}")
print(f"maximum: {maxi}")
print(f"minimum: {mini}")

movies.remove("swarg")
movies.insert(0,"dhol")
print(movies)

nums = [4, 17, -3, 22, 8, -11, 5]
counting = 0
for i in nums:
    if i >0:
        counting = 1+counting
    
print(f"total number of positive numbers: {counting}")

