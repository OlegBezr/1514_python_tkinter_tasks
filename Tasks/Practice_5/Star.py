import time
import sys

def PrintInOnce(l):
    s = ''
    for i in range(len(l)):
        for j in range(len(l[0])):
            s += l[i][j] + ' '
        s = s[:-1]
        s += '\n'
    return s

n = int(input())

l = [['.'] * n for i in range(n)]

if (n % 2) == 0:
    for i in range(0, n):
        print(flush = True)
        l[i][n//2] = '*'
        l[i][n//2 - 1] = '*'
        l[n//2][i] = '*'
        l[n//2 - 1][i] = '*'
        
        print(PrintInOnce(l))
        time.sleep(0.4)
else:
    for i in range(0, n):
        print(flush = True)
        l[i][n//2] = '*'
        l[n//2][i] = '*'
        print(PrintInOnce(l))
        time.sleep(0.5)        

for i in range(n):
    l[i][i] = '*'
    l[n - 1 - i][i] = '*'
    print(flush = True)
    print(PrintInOnce(l))
    time.sleep(0.5)    


#for i in range(n):
   #for j in range(n):
        #print(l[i][j], end = ' ')
    #print()