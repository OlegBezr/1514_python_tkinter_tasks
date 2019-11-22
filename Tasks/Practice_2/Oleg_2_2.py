def FillMatrix(m, n):
    l1 = list()
    for i in range(m):
        l = list()
        for j in range(n):
            l.append(int(input()))
        l1.append(l)
    return l1

def MultMatrix(l1, l2):
    lRes = list()
    for i in range(len(l1)):
        l = list()
        for j in range(len(l2[0])):
            new = 0
            for k in range(len(l1[0])):
                new += l1[i][k] * l2[k][j]
            l.append(new)
        lRes.append(l)
    return lRes
                
                

m = int(input())
n = int(input())
k = int(input())

l1 = FillMatrix(m, n)
l2 = FillMatrix(n, k)

lRes = MultMatrix(l1, l2)

for i in range(len(lRes)):
    for j in range(len(lRes[0])):
        print('%-8d' %lRes[i][j], end = '')
    print()

