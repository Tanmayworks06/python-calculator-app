scores = {"alice": 88, "bob": 45, "charlie" : 92, "diana": 67}
for ki, mark in scores.items():
    if mark >= 60:
        print(f"{ki}, : pass")
       
    else:
        print(f"{ki}, : fail")
