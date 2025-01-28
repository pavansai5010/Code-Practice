count = int(input(":"))
def febo(count):
    k,i=0,0
    j=1
    while k<count:
        s=i+j
        print(s)
        i=j
        j=s
        k=k+1
print(febo(count))        
