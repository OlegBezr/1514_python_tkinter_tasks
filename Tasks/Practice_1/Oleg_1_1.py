a = int(input())
b = int(input())

l = list()

for i in range(1, a + 1):
    l1 = list()
    if(i % 2 == 1):
        for j in range(1, b + 1):
            l1.append(b * (i - 1) + j)
    else:
        for j in range(1, b + 1):
            l1.append(b * i - j + 1)        
    l.append(l1)

for i in range(0, a):
    for j in range(0, b):
        print('%-4d' %l[i][j], end = '')
    print()
        
        