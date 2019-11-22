f = open('numbers.txt', 'r')
l = list(f.read().split())
f.close()

f = open('pos.txt', 'w')
for i in range(len(l)):
    numb = int(l[i])
    sum1 = 0
    while(numb > 0):
        sum1 += numb%10
        numb //= 10
    f.write(str(sum1) + ' ')
f.close()
        