num = int(input("Enter number: "))
if num <=1:
    print(f"{num} is not a prime")
else:
    i=2
    while i<num:
        if num%i == 0:
            print(f"{num} is not a prime number")
            break
        i=i+1
    else:
        print(f"{num} is a prime number")
        
    
