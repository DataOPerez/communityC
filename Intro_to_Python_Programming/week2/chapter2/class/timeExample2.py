#enter a number of seconds and output the equivlant hours, minutes and seconds

#input
startingSeconds = int(input("entere a number of starting seconds: "))

#processing
hours = startingSeconds // 3600
seconds = startingSeconds % 3600

minutes = seconds // 60
seconds = seconds % 60 #seconds %= 60

#output
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"seconds: {seconds}")