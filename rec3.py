def count(n):
    if n>10:
        return
    print(n)
    count(n + 1)
     

count(1)