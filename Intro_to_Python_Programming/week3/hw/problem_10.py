#input from user
percentage = round(float(input("enter a percentage grade: ")))

#if elif statment for each range
if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
else:
    print("F")
