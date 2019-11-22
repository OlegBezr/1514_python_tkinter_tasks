def delete_file(name):
    f = open(name, 'r')
    l = []
    for line in f:
        i = 0
        while (i < len(line)):
            if (line[i] == '+' or line[i] == '-'):
                line = line[:i] + line[i+1:]
                i-=1
            i+=1
        l.append(line)
    f.close()
    
    f = open(name, 'w')
    for i in l:
        f.write(i)
    f.close()

name = input()
delete_file(name)