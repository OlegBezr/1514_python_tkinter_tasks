a, b, c = list(map(int, input().split()))

max1 = (b + (a - 1) * c) * 2 - 1
count = b

l = [] 
for i in range(a):
    for i in range(count):
        stars = (2 * (i + 1) - 1)
        l.append(' ' * ((max1 - stars) // 2) + '*' * stars + ' ' * ((max1 - stars) // 2))
    count += c

for i in l:
    print(i)
    
    