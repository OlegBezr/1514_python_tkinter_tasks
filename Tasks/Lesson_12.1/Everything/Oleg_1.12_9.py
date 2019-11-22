k = int(input())
name = input()

f = open(name, 'r')
l = []
i = 1
for line in f:
    if (i == k - 1):
        line += '\n'
    l.append(line)
    i += 1
f.close()

print(l)

f = open(name, 'w')
for i in l:
    f.write(i)
f.close()