f = open('one.txt', 'r')
l = []
for line in f:
    l.append(line)
f.close()

l.reverse()
l[0] = l[0] + '\n'

f = open('two.txt', 'w')
for i in l:
    f.write(i)
f.close()

