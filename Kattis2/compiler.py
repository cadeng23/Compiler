from sys import stdin
import sys

coms = []

#for line in stdin:
#    coms.append(line)
def lets(str1, varst):
    if str1[1] == ' ':
        tempVar = str1[0]
        print(' 1 char variable')
        a = len(str1) - 4
        new = ''
        for a in range(a, len(str1)):
            new += str1[a]
    ans = arith(new, varst)
    varst[tempVar] = ans
    return varst


def arith(equation, varst):
    arr = []
    while True:
        strr = ''
        for d in range(len(equation) + 1):
            if equation[d] != ' ':
                strr += equation[d]
            if equation[d] == ' ' or d == len(equation) + 1:
                ans = subValue(strr, varst)
                arr.append(ans)
            else:
                arr.append(equation[d])
        break
    while True:
        if arr[1] == '+':
            ans = arr[0] + arr[2]
            arr[2] = ans
            del arr[0],arr[1]
        if arr[1] == '-':
            ans = arr[0] - arr[2]
            arr[2] = ans
            del arr[0],arr[1]
        if arr[1] == '*':
            ans = arr[0] * arr[2]
            arr[2] = ans
            del arr[2]
        if arr[1] == '/':
            ans = arr[0] / arr[2]
            arr[2] = ans
            del arr[2]
        if len(arr) == 1:
            ans = arr[0]
            break
    return ans
            
        

def subValue(subby,varst):
    if subby.isalpha():
        answer = varst.get(subby)
    else:
        answer = int(subby)
    return answer



def sort(coms):
    n = input()
    n = int(n)
    for x in range(n):
        temp = input()
        coms.append(temp)
    for x in range(len(coms) - 1):
        for y in range(len(coms) - x - 1):
            if coms[y] > coms[y + 1]:
                coms[y],coms[y + 1] = coms[y + 1], coms[y]
    return coms

def parse(coms, varst): 
    for x in coms:
        while True:
            if 'LET' in x:
                res = x.index('LET')
                res += 4
                equat = ''
                for t in range(res, len(x)):
                    equat += x[t]
                    print('equation:  ', equat)
                varst = lets(equat, varst)
                break
    return varst




def main():
    coms = []
    varst = {}
    coms = sort(coms)
    varst = parse(coms, varst)
    print(varst)

main()