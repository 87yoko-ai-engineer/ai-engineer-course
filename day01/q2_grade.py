score = int(input("Input your score :"))
if score <0 or score > 100:
     print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")   
elif score >= 60:
    print("D")
else:
    print("E")