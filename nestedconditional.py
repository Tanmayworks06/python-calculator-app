name = input("enter your name: ")
electricity = int(input("total units consumed: "))

if electricity<200:
    print(f"2 rs per unit: {electricity*2}")

elif electricity<400:
    print(f"4 rs per unit: {electricity*4}")

else :
    print(f"6 rs per unit: {electricity*6}")
