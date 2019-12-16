'''
Author: Andres Mrad (Q-ro)
Date: Saturday 14/December/2019 @ 18:54:10
Description:  Solution to the Day 4 puzzle (Part 1) 
'''
_input = "109165-576723"

# Main App


def main():
    passwordRange = tuple(map(int, _input.strip().split('-')))
    possiblePasswordCount = 0
    print(passwordRange[0])
    print(len(str(passwordRange[0])))

    for possiblePassword in range(passwordRange[0], passwordRange[1]+1):
        digitRepeatCount = 0
        passStrVal = str(possiblePassword)
        for i in range(5):
            if int(passStrVal[i]) >= int(passStrVal[i+1]):
                pass
            if int(passStrVal[i]) == int(passStrVal[i+1]):
                digitRepeatCount += 1
            if i == len(passStrVal) and digitRepeatCount > 0:
                possiblePasswordCount += 1
    print(possiblePasswordCount)


# Entry point for the program
if __name__ == "__main__":
    main()
