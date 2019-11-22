f = open('input.txt', 'r')
l = []
for line in f:
    l.append(list(line.split()))
f.close()

ans = 0
for i in l:
    for j in i:
        ans += int(j)

f = open('output.txt', 'w')
f.write(str(ans))
f.close()