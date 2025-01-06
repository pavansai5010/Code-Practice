# mathematical table

num = int(input("Enter a number: "))
steps = int(input("Enter no.of multiples required: "))
def table(num):
    s = 1
    while s<=steps:
        print(f"{num} X {s} = {num*s}")
        s+=1

table(num)
        
        