f = open('text.txt', 'r')
count = 0
for line in f:
    s = line[:-1]
    count += len(s)
    
#В последней строке нет /n, поэтому у меня теряется один символ
count+=1
print(count)
f.close()