#initialize variables
COLUMNS = 5
rows = int(input("Enter the number of rows: "))
pattern = "x"

#loop for each row
for row in range(rows):
    for col in range(COLUMNS): #loop for each column
        print(pattern, end=" ") #print pattern once
        if pattern == "x": #checks if pattern is x if so change to o and vice versa.
            pattern = "o"
        else:
            pattern = "x"
    print("") #space for every row
