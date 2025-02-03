n=input(":")
def ams(n):  
    sum=0
    for i in n:
        sum = sum + (int(i)**3)
    if sum == int(n):
        print(f"{n} is an amstrong number")
    else:
        print(f"{n} is not an amstrong number")
ams(n)