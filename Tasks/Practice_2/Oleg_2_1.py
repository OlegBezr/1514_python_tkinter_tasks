def FillMatrix(m, n):
    l1 = list()
    for i in range(m):
        l = list()
        for j in range(n):
            l.append(int(input()))
        l1.append(l)
    return l1


def MatrixSum (l1, l2):
    lRes = list()
    for i in range(len(l1)):
        l = list()
        for j in range(len(l1[0])):
            l.append(l1[i][j] - l2[i][j])
        lRes.append(l)
    return lRes

m = int(input())
n = int(input())

l1 = FillMatrix(m, n)
l2 = FillMatrix(m, n)

lRes = MatrixSum(l1, l2)

for i in range(m):
    for j in range(n):
        print('%-4d' %lRes[i][j], end = '')
    print()