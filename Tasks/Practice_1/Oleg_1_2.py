a = int(input())
b = int(input())

l = list()

for i in range(a):
    l1 = list()
    l1 = [0] * b
    l.append(l1)

typ = 0
x = 0
y = 0
numb = 1

while(numb <= b * a):
    while (x < b and l[y][x] == 0 and numb <= b * a):
        l[y][x] = numb
        numb += 1
        x += 1
    x -= 1
    y += 1
    
    while (y < a and l[y][x] == 0 and numb <= b * a):
        l[y][x] = numb
        y += 1
        numb += 1
    y -= 1
    x -= 1
    
    while (x > -1 and l[y][x] == 0 and numb <= b * a):
        l[y][x] = numb
        numb += 1
        x -= 1
    x += 1
    y -= 1
    
    while (y > -1 and l[y][x] == 0 and numb <= b * a):
        l[y][x] = numb
        y -= 1
        numb += 1
    y += 1
    x += 1

for i in range(0, a):
    for j in range(0, b):
        print('%-4d' %l[i][j], end = '')
    print()