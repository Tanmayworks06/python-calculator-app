# fav_cities = ("delhi","mumbai","jaipur","udaipur","agra")
# first, *middle, last = fav_cities

# print(f"first city: "  ,first)
# print(f"last city: "  ,last) 


# python = {"riya", "tanmay" , "harnoor"}
# maths = {"riya" , "vansh" , "tanmay"}

# both = python & maths
# print(both)

# x = int(input("enter number: "))
# for i in range(x):
#     i += 1
#     print("*" *i)

# x = int(input("enter number: "))
# for i in range(x,0,-1):
#     print("*" *i)

# x = int(input("enter number: "))
# for i in range(1,x+1):
#     print()
               

di = {
    "name" : "tanmay",
    "age" : 18,
    "subject" : "maths" 
}
di2 = {
    "city" : "jaipur",
    "country" : "japan"
}
print(type(di))
print(di["age"])
di["name"] = "harnoor"
del di["subject"]
di.update(di2)
if "name" in di:
    print("found")

else:
    print("not found")  

print(di.keys())
