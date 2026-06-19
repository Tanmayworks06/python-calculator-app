name = input("acc holder name : ")
acc = input("acc type (saving/current) : ")
bal = float(input("enter opening balance : "))


print(f"NAME : {name}")
print(f"ACC TYPE : {acc}")
print(f"BALANCE : {bal}")


to_do = input("user wants to (withdraw/deposit) : ").lower()
amt = float(input(f"what amount user wants to {to_do} : "))


print(f"you want to {to_do}, rs {amt:.2f}")


if to_do == "withdraw":

    if amt > bal:
        print("insufficient funds")
        new_bal = bal

    else:
        new_bal = bal - amt
        print("withdrawal successful")


elif to_do == "deposit":

    new_bal = bal + amt
    print("deposit successful")


else:

    print("invalid option")
    new_bal = bal


print(f"hello {name}, your account type is {acc}, your new balance is rs {new_bal:.2f}")