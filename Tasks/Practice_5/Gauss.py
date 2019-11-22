def BuildMatrix (n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def MatrixSum (l1, l2):
    lRes = list()
    for i in range(len(l1)):
        lRes.append(l1[i] + l2[i])
    return lRes

def MultRowByNumb (l, n):
    lRes = list()
    for i in range(len(l)):
        lRes.append(l[i] * n)
    return lRes

def FindMaxEl(l):
    max1 = None
    for i in l:
        if (max1 is None or i > max1):
            max1 = i
    return max1

def MethodOfGauss (l):
    ans = [0] * (len(l[0]) - 1)
    
    for i in range(len(l)):
        k = 1
        while (l[i][i] == 0 and i + k < len(l)):
            k += 1
            l[i], l[i + k] = l[i + k], l[i]
        if (l[i][i] != 0):
            l[i] = MultRowByNumb(l[i], 1 / l[i][i])
            for j in range(i+1, (len(l[0]) - 1)): 
                l[j] = MatrixSum(l[j], MultRowByNumb(l[i], -l[j][i]))
    
    Zero = 0
    NoAns = False
    
    for i in range(len(l)):
        if(FindMaxEl(l[i][:-1]) == 0):
            if (l[i][len(l[i]) - 1] != 0):
                NoAns = True
                break
            else:
                Zero += 1
    
    if (NoAns or Zero == 1 and len(l) - Zero > 1):
        return("no")
    elif (len(l) - Zero == 1 and Zero > 0):
        return("many")
    else:
        for i in range(len(l) - 1, -1, -1):
            ans[i] = l[i][len(l)]
            for j in range(i - 1, -1, -1):
                l[j][len(l)] -= l[i][len(l)] * l[j][i] 
                l[j][i] = 0
        return(ans)
        
n = int(input())
l = BuildMatrix(n)

for i in range(n):
    a = int(input())
    l[i].append(a)

ans = MethodOfGauss(l)
if (ans[0] == "n" or ans[0] == "m"):
    print(ans)
else:
    for i in ans:
        print ("%0.5f" %(i))    