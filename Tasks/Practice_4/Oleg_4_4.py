s = input()

x = ord(s[0]) - 95
y = int(s[1]) + 1

a = [['.'] * 12 for i in range(12)]

a[y][x] = 'K'

a[y-2][x-1] = '*'
a[y-2][x+1] = '*'
a[y+2][x-1] = '*'
a[y+2][x+1] = '*'

a[y-1][x-2] = '*'
a[y-1][x+2] = '*'
a[y+1][x-2] = '*'
a[y+1][x+2] = '*'

for i in range(2, 10):
    for j in range(2, 10):
        print(a[i][j], end = '')
    print()