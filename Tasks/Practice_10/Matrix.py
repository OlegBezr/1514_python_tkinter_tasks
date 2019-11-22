def Create(prename, k):
    l = []
    if (k == 1):
        l.append(prename + '0')
        l.append(prename + '1')
    else:
        l.append(Create(prename + '0', k - 1))
        l.append(Create(prename + '1', k - 1))
        
    return l


k = int(input())
print(Create('', k))