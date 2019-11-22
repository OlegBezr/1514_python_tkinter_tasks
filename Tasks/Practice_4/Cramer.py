import copy

def BuildMatrix(n):
    l = list()
    for i in range(n):
        l.append(list(map(int, input().split())))
    return l

def TranspMatrix(l1):
    lRes = list()
    for j in range(len(l1[0])):
        l = list()
        for i in range(len(l1)):
            l.append(l1[i][j])
        lRes.append(l)
    return lRes

def MinorMatrix(l, x, y):
    lRes = list()
    for i in range(len(l)):
        if (i != x):
            lRes.append(l[i][:y] + l[i][y+1:])
    return lRes

def OpredMatrix(l):
    if (len(l) == 1):
        return l[0][0]
    else:
        Opred = 0
        for j in range(len(l)):
            Opred += pow(-1, j) * l[j][0] * OpredMatrix(MinorMatrix(l, j, 0))
        return Opred
    
def MethodOfCramer(Coef, Res):
    Coef = TranspMatrix(Coef)
    Res = TranspMatrix(Res)
    
    Opred1 = OpredMatrix(Coef)
    
    ans = []
    
    for i in range(len(Coef)):
        new = copy.deepcopy(Coef)
        new[i] = Res[0]
        ans.append(OpredMatrix(new))
    
    if (Opred1 == 0):
        check = True
        for i in ans:
            if (i != 0):
                check = False
        if (check):
            return ("many")
        else:
            return ("no")
    else:    
        for i in range(len(ans)):
            ans[i] /= Opred1
        return ans
    
    
n = int(input())
Coef = BuildMatrix(n)
Res = BuildMatrix(n)

ans = MethodOfCramer(Coef, Res)
if (ans[0] != 'm' and ans[0] != 'n'):
    for i in ans:
        print ("%0.5f" %(i))
else:
    print(ans)