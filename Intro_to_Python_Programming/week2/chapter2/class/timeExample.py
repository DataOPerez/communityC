#input hours minutes and seconds, and display totla number of seconds

#input information
hours = int(input("enter a number of hours: "))
minutes = int(input("enter a number of minutes: "))
seconds = int(input("enter a number of seconds: "))
totalNumberOfSeconds = 0


#process our informaiton
secondsInHours = hours * 3600
secondsInMinutes = minutes * 60
totalNumberOfSeconds = secondsInHours + secondsInMinutes + seconds


#output our information

print(f"\n total number of seconds is: {totalNumberOfSeconds}")