def FillSquareMatrix(m):
    l1 = list()
    for i in range(m):
        l = list()
        l1.append(list(map(int, input().split())))
    return l1

def TranspMatrix(l1):
    lRes = list()
    for j in range(len(l1[0])):
        l = list()
        for i in range(len(l1)):
            l.append(l1[i][j])
        lRes.append(l)
    return lRes

m = int(input())

l1 = FillSquareMatrix(m)

lRes = list()
lRes = TranspMatrix(l1)

#print(lRes)

for i in range(len(lRes)):
    for j in range(len(lRes[0])):
        print('%-4d' %lRes[i][j], end = '')
    print()