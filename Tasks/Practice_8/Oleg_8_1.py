f = open('input.txt', 'r')
l = []
for line in f:
    l.append(list(line.split()))

for i in l:
    i.reverse()
f.close()

f = open('output.txt', 'w')
for i in l:
    f.write(' '.join(i) + '\n')
f.close()
    