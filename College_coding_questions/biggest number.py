n = input(":")
b = n[0]
for i in range(1,len(n)):
    if b < n[i]:
        b = n[i]
print(b)