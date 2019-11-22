def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def MinorMatrix(l, x, y):
    lRes = list()
    for i in range(len(l)):
        #print(l[:y] + l[y+1:])
        if (i != x):
            lRes.append(l[i][:y] + l[i][y+1:])
    return lRes

n = int(input())
l = BuildMatrix(n)
x = int(input())
y = int(input())

if (x >= 0 and x < len(l) and y >= 0 and y < len(l[0])):
    ans = MinorMatrix(l, x, y)
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            print("%-d" %(ans[i][j]), end = ' ')
        print()
else:
    print(-1)