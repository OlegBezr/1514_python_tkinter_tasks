f = open('input.txt', 'r')
l = []
for line in f:
    l.append(list(line.split()))
f.close()

ans = 0
for i in l:
    ans += len(i)

f = open('output.txt', 'w')
f.write(str(ans))
f.close()