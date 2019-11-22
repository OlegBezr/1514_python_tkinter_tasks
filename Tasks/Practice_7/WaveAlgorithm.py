def BuildMatrix():
    f = open('input.txt', 'r')
    for line in f:
        l.append(list(map(int, line)))
    f.close()
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


M1 = BuildMatrix()

ans = FindAllDist(M1)

f = open('output.txt', 'w')

for i in range(n):
    for j in range(n):
        f.write(ans[i][j] + ' ')
    f.write('\n')

f.close()