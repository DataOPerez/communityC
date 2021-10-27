
stop = "y"
#if elif statment for each range

while stop == "y" or stop == "Y":
    percentage = round(float(input("enter a percentage grade: ")))

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

    print("\n")
    stop = input("Would you like to enter another grade? (Y/N) ") #asks the user if they would like to continue.
print("Grading Stopped")
