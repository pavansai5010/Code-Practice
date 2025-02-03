a=int(input(":"))
b=int(input(":"))
c=int(input(":"))
if a == b == c:
    print("all are equal")
elif a>b:
    if a>c :
        print(f"{a} is greater number")
    else:
        print(f"{c} is greater number")
elif b>c :
    print(f"{b} is greater")
else :
    print(f"{c} is greater")