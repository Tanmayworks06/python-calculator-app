name = input("student name:")
roll_number = int(input("enter your roll no.:"))
english = float(input("english marks out of 100:"))
maths = float(input("maths marks out of 100:"))
chemistry = float(input("chemistry marks out of 100'"))
physics = float(input("physics marks out of 100:"))
music = float(input("music marks out of 100:"))

print(f"calculated marks marks:{english+maths+physics+chemistry+music}")

calculated_marks = float(input("enter calculated marks:"))
total_marks = 500
percentage = (calculated_marks/total_marks) * 100

print(f"{percentage}%")

average = (english+maths+physics+chemistry+music)/5

print(f"average:{average}")


a = percentage>=40 
print(a)


