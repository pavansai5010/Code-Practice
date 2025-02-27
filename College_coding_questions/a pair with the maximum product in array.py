n=int(input("-"))
arr=[]
for i in range(n):
    arr.append(int(input()))
pairs=[]
for i in range(n):
    for j in range(i+1,n):
        