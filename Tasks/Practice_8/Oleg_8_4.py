# -*- coding: cp1251 -*-

def findAtoB(lab, sx, sy):
    s1 = len(lab)
    s2 = len(lab[0])
    
    w = [[sy, sx]]
    f = [[sy, sx]]
    
    yes = False
    
    help = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    
    while (len(f) > 0 and not yes):
        newF = list()
        for i in f:
            if(yes):
                break
            
            for j in help:
                check = lab[i[0] + j[0]][i[1] + j[1]]
                add = [i[0] + j[0], i[1] + j[1]]
                if((check == '.' or check == 'f') and not add in w):  
                    w.append(add)
                    newF.append(add)            
                    
                if(check == 'f'):
                    #print('FOUND')
                    yes = True
                    break
        f = newF
     
    if (yes):
        w.reverse()
        count = 0
        last_old = w[0]
        last = w[0]


        for i in w:
            for j in help:
                if (i ==  [last[0] + j[0], last[1] + j[1]]):
                    last = [i[0], i[1]]
                    break
                
            if(last_old != last):
                count += 1
                last_old = last
                
            lab[last[0]][last[1]] = '*'
            
        s = w[len(w) - 1]
        f = w[0]
        lab[s[0]][s[1]] = 's'
        lab[f[0]][f[1]] = 'f'
        
        return count
    else:
        return('No')


f = open('input.txt', 'r')
lab = []

for line in f:
    numb = len(line)
    lab.append(['X'] * (numb + 1))
    break
f.close()

f = open('input.txt', 'r')

for line in f:
    l_new = []
    for i in line:
        if(i != '\n'):
            l_new.append(i)
    lab.append(['X'] + l_new + ['X'])

lab.append(['X'] * (numb + 1))
f.close()

s1 = len(lab)
s2 = len(lab[0])

sx = 0
sy = 0

fx = 0
fy = 0

for i in range(s1):
    for j in range(s2):
        if (lab[i][j] == 's'):
            sx = j
            sy = i
        elif (lab[i][j] == 'f'):
            fx = j
            fy = i        

ans = findAtoB(lab, sx, sy)
f = open('output.txt', 'w')
if (ans == 'No'):
    f.write('Пути нет')
else:
    f.write(str(ans) + '\n')
    lab = lab[1:-1]
    for i in lab:
        f.write(''.join(i[1:-1]) + '\n')    

f.close()
