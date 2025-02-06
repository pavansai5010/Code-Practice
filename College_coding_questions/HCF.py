n1 = int(input(":"))
n2 = int(input(":"))
def hcf(n1,n2):
    Min = min(n1,n2)
    s=1
    for i in range(1,Min+1):
        if n1%i==0 and n2%i==0:
            s=s*i
    return(s)
print(hcf(n1,n2))