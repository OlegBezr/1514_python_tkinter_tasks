n, m = list(map(int, input().split()))

table = [[0] * (m + 2) for i in range(n + 2)]

help = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

numb = int(input())

for i in range(numb):
    a, b = list(map(int, input().split()))
    table[a][b] = '*' 
    
for i in range(1, n + 1):
    for j in range(1, m + 1):
        count = 0
        if (table[i][j] != '*'):
            for k in help:
                if (table[i + k[0]][j + k[1]] == '*'):
                    count += 1
            table[i][j] = count
        
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(table[i][j], end = ' ')
    print()