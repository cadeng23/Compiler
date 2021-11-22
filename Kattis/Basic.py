from sys import stdin
from enum import Enum

class Commands(Enum):
    LET = 1
    IF = 2
    PRINT = 3
    PRINTLN = 4

#the two lines below are for the final code
def setarr(arr):
    #for x in stdin:
    #   arr.append(x)
    for a in range(1):
        k = input()
        arr.append(k)
    #return arr

def sortlines(arr, order):
    for a in arr:
        if ' ' == a[2]:
            str = a[0] + a[1]
            str = int(str)
            order.append(str)
        if ' ' == a[3]:
            str = a[0] + a[1] + a[2]
            str = int(str)
            order.append(str)
        if ' ' == a[4]:
            str = a[0] + a[1] + a[2] + a[3] 
            str = int(str)
            order.append(str)
    for x in range(0, len(order)-1):
        for y in range(0, len(order)-x-1):
            if order[y] > order[y + 1]:
                #order[y], order[]
                order[y],order[y+1] = order[y+1],order[y]
                arr[y],arr[y+1] = arr[y+1], arr[y]
    return arr, order

#setarr(arr)
#arr = sortlines(arr, order)

def Command(str):
    com = ''
    if 'PRINT' in str:
        pos = str.find('PRINT') + 5
        rest = len(str) - pos
        for a in range(len(str)):
            if a > pos:
                com += str[a]
        print(com)
    if 'LET' in str:
        pos = str.find('LET') + 3
        rest = len(str) - pos
        for a in range(len(str)):
            if a > pos:
                com += str[a]
        if len(com) == 5:
            temp = com[0]
            
            


def main():
    arr = []
    order = []
    setarr(arr)
    arr, order = sortlines(arr, order)
    print('\n')
    for x in arr:
        com = Command(x)

main()