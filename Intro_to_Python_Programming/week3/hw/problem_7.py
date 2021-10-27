#same as the last just add an input for the number of rows
size = int(input("How many rows of starts would you like to see: "))


for row in range(size):
    for column in range(row + 1): 
        print("*", end="") 
    print("")
