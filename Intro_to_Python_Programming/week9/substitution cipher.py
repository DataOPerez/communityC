from ctypes import c_char
from hashlib import new
import pickle
import random


def openEncryptedMessage(filename="EncryptedMessage.txt"):
    """Loads the encrypted text file and returns its contents"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    return contents


def buildCipher() -> dict:
    '''Build a random cipher'''
    cipher = {} # empty dictionary

    for key in range(97, 123): # for loop starting at 97 stops at 122.
        randomValue = chr(random.randint(97,122)) # assign a random ASCII value to this variable

        while randomValue in cipher.values(): # check if the value exists in our dictionary as a value
            randomValue = chr(random.randint(97, 122)) # if it does then assign a new value to the variable until it isn't in our dictionary.
        
        cipher[chr(key)] = randomValue # once it passes the while loop check assign the key to the value within our dictionary.
    
    return cipher


def encryptMessage(text: str, cipher: dict):
    '''Encrypt message from the "text" parameter using our build cipher'''
    newMessage = "" # new blank message

    for ch in text.lower(): # iterates through each letter in our text
        newMessage += cipher.get(ch, ch) # Find new letter via our cipher dictionary and concatenate it to the newMessage variable.

    return newMessage


def loadCipher(fileName: str):
    input_file = open(fileName, "rb")
    object = pickle.load(input_file)
    print(object)
    return object

    pass  # Remove pass instruction and write your function definition here


def decrypt(text: str, cipher: dict):
    '''Decrypt message from the "text" parameter using our build cipher'''
    newMessage = "" 
    valueList = list(cipher.values()) # turn all the values in a list
    keyList = list(cipher.keys()) # turn all the keys into a list

    for ch in text.lower(): # for loop for each character in text parameter.lower
        if ch in cipher.values(): # this if statement will ignore any letters and return the character to the newMessage variable.
            index = valueList.index(ch) # if the character is in our cipher values we get the key
            newMessage += keyList[index] # and concatenate it to our 
        else:
            newMessage += ch

    return newMessage # return the new message


def main():
    """ Test Area
        Remove or add comments for functions to test
    """
    print("TESTING PART 1")
    #### Remove comments to test buildCypher function ####
    cipher = buildCipher()
    print(cipher)  # displays your cypher

    #### Remove comments to test encryptMessage Function ####
    message = "The Quick Brown Fox, Jumps Over the lazy Dog"
    encryptedMessage = encryptMessage(message, cipher)
    print(encryptedMessage)

    # Part 2
    print("\nTesting Part 2")
    #### Remove Comments to test decrypt function ####
    decryptedMessage = decrypt(encryptedMessage, cipher)
    print(decryptedMessage)

    #### Remove comments to test loadCypher Function ####
    new_cipher = loadCipher("cipher.dat")
    print(decrypt(openEncryptedMessage(), new_cipher))


if __name__ == '__main__':
    main()
