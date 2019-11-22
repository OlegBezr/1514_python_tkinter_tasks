name = input()
f = open(name, 'r')

l = []

for line in f:
    if('\n' in line):
        line = line[:-1]
    l.append(line)
f.close()

f = open(name, 'w')
for i in l:
    f.write(i)
f.close()