SIZE = 5

#this was harder for me to understand. had to go over it a couple of times.
#let's say we are on our third iteration of this program
for row in range(SIZE): #row becomes 2 (since we started from 0)
    for column in range(row + 1): #column becomes 3 (row+1)
        print("*", end="") #this will print once star then go back up to the "for column" loop to finish its other two iterations".
    print("")
