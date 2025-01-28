string=input("Enter a string: ")
s=[]
l=len(string)
for i in range(l):
    for j in range(i+1,l+1):
        n=string[i:j]
        s.append(n)
print(s)