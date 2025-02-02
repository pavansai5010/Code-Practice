num = input(":")
def high_substring(num):
    l=[]
    for i in range(len(num)):
        for j in range(i+1,len(num)+1):
            l.append(int(num[i:j]))
    for k in l:
        if int(k)%2 == 0:
            l.remove(k)
    return str(max(l))
print(high_substring(num))