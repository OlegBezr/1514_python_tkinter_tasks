def TranspMatrix(l1):
    lRes = list()
    for j in range(len(l1[0])):
        l = list()
        for i in range(len(l1)):
            l.append(l1[i][len(l1[0]) - 1 - j])
        #print(l)
        lRes.append(l)
    return lRes

def FindMaxEl(l):
    max1 = None
    for i in l:
        if (max1 is None or i > max1):
            max1 = i
    return max1

l = list(map(int, input().split()))

max1 = FindMaxEl(l)

ans = []
ans.append(['*'] * (max1 + 2))

for i in l:
    ans.append(['*'] * i + [' ']*(max1 - i + 1) + ['*'])

ans.append(['*'] * (max1 + 2))

#print(ans)

ans = TranspMatrix(ans)

f = open('output.txt', 'w')

for i in ans:
    f.write(''.join(i) + '\n')

f.close()

