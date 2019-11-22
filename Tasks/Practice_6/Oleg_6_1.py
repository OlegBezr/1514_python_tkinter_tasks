def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def GetSegMatrixByDist(l):
    n = len(l)
    ans = list()
    
    for i in range(n):
        for j in range(n):    
            if(i < j and l[i][j] == 1):
                ans.append([i + 1, j + 1])
    return ans

n = int(input())

dist = BuildMatrix(n)
ans = GetSegMatrixByDist(dist)

for i in ans:
    print(*i)
