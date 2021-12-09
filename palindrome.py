full = 'Banana'
new = []
startlen = 6
for x in full:
    new.append(x)
def iterate(new):
    for x in range(startlen):
        if new == new[::-1]:
            print('Complete!!!')
            pThrough(new)
            break
        if new != new[::-1]:
            del new[0]
def pThrough(new):
    for i in new:
        print(i, end = '')
    print(' is now a palendrome!')
iterate(new)