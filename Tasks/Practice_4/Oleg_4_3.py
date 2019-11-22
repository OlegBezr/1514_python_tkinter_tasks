n = int(input())
m = int(input())

A = [ [0] * m for i in range(n) ]

star = False
for i in range(len(A)):
    for j in range(len(A[0])):
        if (j % 2 == 0 and star or j % 2 == 1 and not star):
            A[i][j] = '*'
            print(A[i][j], end = '')
        else:
            A[i][j] = '.'
            print(A[i][j], end = '')
    print()
    star = not star

