a, b = list(input().split('x'))

a = int(a)
one, two = b.split()
b = int(one + two)

first, last = list(map(int, input().split(',')))

f = open('output.txt', 'w')
for i in range(first, last + 1):
    print (i, '->', i * a + b, file = f)
f.close()