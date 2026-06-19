#Q9
# def remove_duplicates_ordered(lst):
#     seen = set()
#     result = []


#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
    
#     return result

# list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(remove_duplicates_ordered(list))


#Q10
cart = []
def add_items():
    name=input("enter item name: ")
    price=float(input("enter item price:  "))

    item = {'Item': name , 'Price': price}
    cart.append(item)
    print(f"{name} added to cart.\n")

def remove_items():
    name = input("Enter item name that you want to remove:  ")

    for item in cart:
        if item["Item"] == name:
            cart.remove(item)
            print(f'{name} is removed from your list')
            return
        
        
    print("item not found in your list")

def display_items():
    if len(cart)==0:
        print("your cart is empty")
        return
    
    total = 0
    print("-----Items in cart-----")
    for item in cart:
        print(item['Item'],"-",item['Price'])
        total += item["Price"]

    print("Total price:", total)

while True:
    print("\n1. add item")
    print("2. remove item")
    print("3. display cart")
    print("4. quit")

    choice = (input("Enter choice: "))
    if choice == "1":
        add_items()
    elif choice == "2":
        remove_items()
    elif choice == "3":
        display_items()
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("invalid choice")    
          
