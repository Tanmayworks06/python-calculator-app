try:
    data = input("Enter number using commas: ")
    num = data.split(",")
    total = 0
    for items in num:
        total +=int(items)

    avg = total/(len(num))
    print("average =",avg)

except ValueError:
    print("invalid data")

    
    