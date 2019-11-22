help = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def DFS(y, x):
    l[y][x] = 0
    for j in help:
        if (l[y + j[0]][x + j[1]] == 1):
            DFS(y + j[0], x + j[1])
            

n, m = list(map(int, input().split()))

l = [[0] * (m + 2)]
 
for i in range(n):
    l.append([0] + list(map(int, input().split())) + [0])

l.append([0] * (m + 2))

count = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (l[i][j] == 1):
            count += 1
            DFS(i, j)

print(count)