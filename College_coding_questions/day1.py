'''
This function return a number if it is a prime number.
prime number: If a number is having only 1 and itself as their factors, then it is called a prime number.
'''
def prime_num(num):
    if num <=1 :
        print(f"{num} is not a prime number.")
    
    for i in range(2,(int(num**0.5))+1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
    
'''
This function returns the corresponding age group.

'''
def AGE(age):
    if age <= 12:
        print("You belongs to -Child category-")
    elif 12<age<=19:
        print("You belongs to -Teenage category-")
    elif 19<age<=64:
        print("You belongs to -Adult category-")
    else:
        print("You belongs to -Senior category-")

#num = int(input("Enter a number to find it is prime or not: "))

#prime_num(num)


age = int(input("If you want to know your age group, Enter your age:"))

AGE(age)