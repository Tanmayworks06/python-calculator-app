# dict = {
#     "Name" : "Tanmay",
#     "age" : 18,
#     "city" : "jaipur",
#     "hobby" : "photography",
#     "language" : "hindi"
# }

# for ki, value in dict.items():
#     print(f"{ki} : {value}")


# text = "the cat sat on the mat the cat"
# words_c = {}
# for word in text.split():
#     if word in words_c:
#         words_c[word] += 1
#     else:
#         words_c[word] = 1
    
# print(words_c)

countries = {
    "INDIA" : "DELHI",
    "BRAZIL" : "BRASILIA",
    "EGYPT" : "CAIRO"
}

countries["JAPAN"] = "TOKYO"


countries.pop("EGYPT")


print("INDIA" in countries)
print(countries)


a = sorted(countries.values())
print(a)



# students = {}

# for i in range(5):
#     name = input("enter name : ")
#     marks = int(input("enter makrs : "))
#     students[name] = marks

# for name in students:
#     if students[name] >= 50:
#         print(f"{name} , {marks} , PASS")
#     else:
#         print(f"{name} , {marks} , FAIL")  

# student = [
#     {"name" : "tanmay" , "score" : 90}
#     {"name" : "harnoor" , "score" : 20}
#     {"name" : "vansh" , "score" : 50} 
# ]

 