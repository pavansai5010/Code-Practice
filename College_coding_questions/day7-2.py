n=[2,2,1,1,5,6,2,48,6,5,5]
def single(n):
    d = dict()
    for i in n:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    for key in d:
        if d[key] == 1:
            return key
    
print(single(n))
