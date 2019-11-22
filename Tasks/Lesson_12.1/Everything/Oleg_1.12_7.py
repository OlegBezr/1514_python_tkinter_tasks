n, k = input().split()
n = int(n)
k = int(k)

s = '*' * k + '\n'
f = open('star.txt', 'w')
for i in range(n):
    f.write(s)
f.close()
