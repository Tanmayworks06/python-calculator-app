def diamonds(n):
    for i in range(1,n+1,2):
       space = " " * ((n-i) // 2)
       print(space + "*" * i)

    # for i in range(n-2,0,-2):
    #     space = " " * ((n-i) // 2)
    #     print(space + "*" * i)

diamonds(5)