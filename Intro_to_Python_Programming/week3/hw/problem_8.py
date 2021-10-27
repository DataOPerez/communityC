#setup a flag
isPrime = True

#first loop get our range of numbers
for i in range(2, 100):
    isPrime = True #setting our loop to true one more time
    for previousNumber in range(2, i): #second loops uses previous numbers to % against current number
        if i % previousNumber == 0: #if remainder is 0 the number isn't prime.
            isPrime = False #set flag to false

    if isPrime: #check flag outside of first loop if prime is true print prime number
        print(i)

