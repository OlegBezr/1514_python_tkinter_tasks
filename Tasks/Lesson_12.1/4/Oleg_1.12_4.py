file = input()
clas = input()

f = open(file, 'r')

no = True

for line in f:
    l = list(line.split())
    if (l[0] == clas):
        print(line)
        no = False
        break

if no:
    print('Not found')

f.close()
