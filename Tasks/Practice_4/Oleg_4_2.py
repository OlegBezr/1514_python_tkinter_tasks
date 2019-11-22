def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def FindMaxEl(l):
    max1 = None
    posY, posX = 0, 0
    
    for i in range(len(l)):
        for j in range(len(l[0])):
            if (max1 is None or l[i][j] > max1):
                max1 = l[i][j]
                posX, posY = i, j
                
    return posX, posY

n = int(input())
m = int(input())

l = BuildMatrix(n)

print(*FindMaxEl(l))
