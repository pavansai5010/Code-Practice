n = int(input(":"))
def perfect_number(n):
    c=0
    for i in range (1,n):
        if n%i == 0:
            c=c+i
    if n == c :
        return True
    else:
        return False
print(perfect_number(n))    