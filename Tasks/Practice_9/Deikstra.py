def BuildMatrix():
    l = []
    f = open('input.txt', 'r')
    for line in f:
        l.append(list(map(int, line.split())))
    f.close()
    return l

def ChangeNeighbours(a, line):
    for i in range(len(M[a])):
        if (M[a][i] != -1):
            new_v = M[a][i] + line[a]
            if (new_v < line[i]):
                line[i] = new_v
                
def FindAllWays(a):
    current = a
    line = [max1] * n
    viewed[a] = True
    line[a] = 0
    ChangeNeighbours(current, line)
    
    min_pos = 1
    
    while (not min_pos is None):
        min1 = max1
        min_pos = None
        for i in range(n):
            if (line[i] < min1 and not viewed[i]):
                min1 = line[i]
                min_pos = i
        if (not min_pos is None):
            viewed[min_pos] = True
            ChangeNeighbours(min_pos, line)
    return line

M = BuildMatrix()
max1 = 1000000000

n = len(M)

f = open('output.txt', 'w')
for i in range(n):
    viewed = [False] * n
    ans = FindAllWays(i)
    for j in ans:
        print('%2d' %(j), end = '  ', file = f)
    print(file = f)
f.close()

