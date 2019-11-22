l = list(input().split())

f = open('list1.txt', 'w')
f.write(' '.join(l))
f.close()

f = open('list1.txt', 'r')
l = list(f.read().split())
f.close()

f = open('list2.txt', 'w')
for i in range(len(l)):
    if (i % 2 == 1):
        f.write(l[i] + ' ')
f.close()
