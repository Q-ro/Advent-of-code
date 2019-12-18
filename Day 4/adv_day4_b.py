'''
Author: Andres Mrad (Q-ro)
Date: Tuesday 17/December/2019 @ 18:24:49
Description:  Solution to puzzle 4 (Part 2)
'''

# import
import itertools

_input = "109165-576723"

# ====== Filters

# Going from left to right, the digits never decrease; they only ever
def filterDigitIncrease(password):
    for i in range(len(password)-1):
        if int(password[i]) > int(password[i+1]):
            return False

    return True

# the two adjacent matching digits are not part of a larger group of matching digits.
def noGroupFilter(password):    
    for group in [list(group) for k,group in itertools.groupby(password)]:
        if len(group) == 2:
            return True
    return False

def passwordPossibilityCounter(passwordRangeStart, passwordRangeEnd):
    possiblePasswordCount = 0
    print(passwordRangeStart)
    print(len(str(passwordRangeStart)))

    for possiblePassword in range(passwordRangeStart, passwordRangeEnd+1):
        passStrVal = str(possiblePassword)
        # It is a six-digit number.
        if len(passStrVal) != 6:
            continue
        # Evaluate if the number combination is a valid password
        if filterDigitIncrease(passStrVal) and noGroupFilter(passStrVal):
            possiblePasswordCount += 1

    return possiblePasswordCount

# Main app


def main():
    passwordRangeStart, passwordRangeEnd = map(int, _input.strip().split('-'))
    print(passwordPossibilityCounter(passwordRangeStart, passwordRangeEnd))


if __name__ == "__main__":
    main()
