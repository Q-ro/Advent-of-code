'''
Author: Andres Mrad (Q-ro)
Date: Tuesday 03/December/2019 @ 17:02:04
Description:  Custom python implementations of common helpers
'''

# custom Map implementation
def customMap(func, arr):
    tempArray = []
    for x in arr:
        tempArray.append(func(x))
        pass
    return tempArray