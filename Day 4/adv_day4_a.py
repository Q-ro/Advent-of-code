'''
Author: Andres Mrad (Q-ro)
Date: Saturday 14/December/2019 @ 18:54:10
Description:  Solution to the Day 4 puzzle (Part 1) 
'''

_input = "109165-576723"


# ====== Filters

# Going from left to right, the digits never decrease; they only ever 
def filterDigitIncrease(password):
    for i in range(len(password)-1):
        if int(password[i]) > int(password[i+1]):
            return False

    return True

# Two adjacent digits are the same (like 22 in 122345)
def filterDoubleDigit(password):
    digitRepeatCount = 0
    for i in range(len(password)-1):
        if int(password[i]) == int(password[i+1]):
            digitRepeatCount += 1
    
    if digitRepeatCount > 0:
        return True
    
    return False

def passwordPossibilityCounter(passwordRangeStart,passwordRangeEnd):
    possiblePasswordCount = 0
    print(passwordRangeStart)
    print(len(str(passwordRangeStart)))

    for possiblePassword in range(passwordRangeStart, passwordRangeEnd+1):
        passStrVal = str(possiblePassword)
        # It is a six-digit number.
        if len(passStrVal) != 6:
            continue
        # Evaluate if the number combination is a valid password
        if filterDigitIncrease(passStrVal) and filterDoubleDigit(passStrVal):
            possiblePasswordCount += 1

    return possiblePasswordCount

# Main App
def main():
    passwordRangeStart, passwordRangeEnd = map(int, _input.strip().split('-'))
    print(passwordPossibilityCounter(passwordRangeStart,passwordRangeEnd))


# Entry point for the program
if __name__ == "__main__":
    main()
