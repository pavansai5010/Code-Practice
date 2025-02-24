n = input()
l=[]
for i in range(len(n)):
    if i%2!=0:
        l.append(n[i])
for j in n:
    if j not in l:
        l.append(j)
print("".join(l))