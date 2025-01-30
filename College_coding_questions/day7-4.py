n=int(input(":"))
def unknown(n):
    l=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            l.append("FizzBuzz")
        elif i%3==0 and i%5!=0:
            l.append("Fizz")
        elif i%3!=0 and i%5==0:
            l.append("Buzz")
        else:
            l.append(i)
    return l
print(unknown(n))