def fact(i):
    if i<=1:
        return 1
    else:
        return i*(fact(i-1))

num=input(":")
s=0
for i in num:
    s = s + fact(int(i))
if s == num:
    print("it is a strong")
else:
    print("not a strong number")