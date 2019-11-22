def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def MinorMatrix(l, x, y):
    lRes = list()
    for i in range(len(l)):
        if (i != x):
            lRes.append(l[i][:y] + l[i][y+1:])
    return lRes

def OpredMatrix(l):
    if (len(l) == 1):
        return l[0][0]
    else:
        Opred = 0
        for j in range(len(l)):
            Opred += pow(-1, j) * l[0][j] * OpredMatrix(MinorMatrix(l, 0, j))
        return Opred

n = int(input())
l = BuildMatrix(n)
print(OpredMatrix(l))