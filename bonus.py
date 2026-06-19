students = [
    {"name":"Tanmay","score" : 90},
    {"name":"harnoor","score" : 88},
    {"name":"vansh","score" : 85}
]

high_scorer = students[2]

for student in students:
    if student["score"] > high_scorer["score"]:
        high_scorer = student 

print(f"highest scorer :  {high_scorer['name']}")
print(f"score :  {high_scorer['score']}")
