def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l


def FindAllDist(l):
    n = len(l)
    dist = [[-1] * n for i in range(n)]
    
    for this in range(n):
        dist[this][this] = 0
        w = [this]
        f = [this]
        C = 0   
        while (len(f) > 0):
            newF = list()
            for i in f:
                for j in range(len(M1[i])):
                    if (M1[i][j] == 1 and not j in w):  
                        w.append(j)
                        newF.append(j)
                        dist[this][j] = C + 1
            C += 1
            f = newF    
    return dist


n = int(input())
M1 = BuildMatrix(n)

ans = FindAllDist(M1)

for i in range(n):
    for j in range(n):
        print('%4d' %ans[i][j], end = '')
    print()