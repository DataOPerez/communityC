#functions
def formatData(information: str):
    '''
    This will format the data:
    - Upper case letters
    - Remove white space before and after string
    '''
    information = information.upper()
    information = information.strip()

    return information

def getFirstName(fullName: str):
    '''This will return someone's first name when given a full name.'''
    firstSpace = fullName.find(" ")

    fullName = fullName[0 : firstSpace]
    #print(fullName)
    return fullName

def getLastName(fullName: str):
    nameList = fullName.split()
    
    #print(nameList[-1])
    return nameList[-1]

def validateEmai(emailAddress: str):
    '''
    This will validate an email address based on the following:
    - Include the @ symbol
    - Must end in
        - .com
        - .org
        - .net
    '''
    
    atSymoblCheck = emailAddress.find('@')
    if atSymoblCheck == -1:
        atSymoblCheck = False
    else:
        atSymoblCheck = True

    endingCheck = emailAddress.endswith(('.com', 'org', '.net'))

    if atSymoblCheck and endingCheck:
        return True
    else:
        return False

    
def validatePhoneNumber(number: str):
    '''
    The function will validate the phone number by:
    - Checking for 10 digits
    - Checking for 12 characters
    - Checking for format:
        - 3 digits, a “-”, 3 digit, a “-” 4 digits 
    '''
    totalLength = True
    totalDigits = True
    correctFormat = True

#checks if 12 characters total
    if len(number) < 12:
        totalLength = False 

#checks if 10 digits
    counter = 0
    for ch in number:
        if ch.isdigit():
            counter += 1
    if counter < 10:
        totalDigits = False
        
#checks for formatting
    splitNumber = number.split('-') #split the string by '-'
    
    if len(splitNumber) != 3: #checks if the splitNumber has three sequences
        correctFormat = False
    else:
        for str in splitNumber: #for each sequence check if == 3 else if == 4 else set format to False.
            if len(str) == 3:
                pass
            elif len(str) == 4:
                pass
            else:
                correctFormat = False

#Checks if all checks are true return true or false
    if totalLength and totalDigits and correctFormat:
        return True
    else:
        return False


def validatePassword(password: str):
    '''
    This function will validate password
    - The password contains at least 10 characters
    - Has at least:
        - 1 lowercase letter
        - 1 uppercase letter
        - 1 digit
    - Has at least 1 special symbol from the following: ! @ # $ % ^ & * ( ) ?
    '''
    SPECIAL_CHAR = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?')
    lengthCheck = False
    lowerCheck = False
    upperCheck = False
    digitCheck = False
    specialCheck = False

    if len(password) >= 10:
        lengthCheck = True

    for ch in password:
        if ch.islower():
            lowerCheck = True
        elif ch.isupper():
            upperCheck = True
        elif ch.isdigit():
            digitCheck = True

    for ch in password:
        if ch in SPECIAL_CHAR:
            specialCheck = True


    if lengthCheck and lowerCheck and upperCheck and digitCheck and specialCheck:
        return True
    else:
        print('Length', lengthCheck)
        print('Lower: ', lowerCheck)
        print('Upper: ', upperCheck)
        print('Digit: ', digitCheck)
        print('Special: ', specialCheck)
        return False




#---main---
def main():
    '''Runs all the functions'''

    data = '      banana      '
    fullName = 'Oscar Ismael Perez'
    email = 'Oscar.Perez1919@yahoo.com'
    phoneNumber = '630-639-7930'
    password = 'Password1234!'

    formatDataResult = formatData(data)
    getFirstNameResult = getFirstName(fullName)
    getLastNameResult = getLastName(fullName)
    validateEmaiResult = validateEmai(email)
    validatePhoneNumberResult = validatePhoneNumber(phoneNumber)
    validatePasswordResult = validatePassword(password)

    print('\t--- Validated information ---')
    print('Data:', formatDataResult)
    print('First Name:', getFirstNameResult)
    print('Last Name:', getLastNameResult)
    print('Valid Email:', validateEmaiResult)
    print('Valid Phone Number:', validatePhoneNumberResult)
    print('Valid Password:', validatePasswordResult)


if __name__ == '__main__':
    main()
