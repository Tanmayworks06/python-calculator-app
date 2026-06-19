def sum_num(n):
    if n == 0:
        return 0
    else:
        return n + sum_num(n-1)
num = int(input("Enter number: "))    
print(sum_num(num))