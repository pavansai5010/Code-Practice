'''1.You have a number to examine, and your mission is to write a program that checks 
whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 
27?'''

def multiple():
    n=int(input(":"))
    if n%27 == 0:
        print(f"{n} is a multiple of 27")
    else:
        print(f"{n} is not a multiple of 27")
        
# multiple() # function call

'''2.You have two numbers, and your challenge is to write a program that performs both 
addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results?'''

num1=int(input("num1: "))
num2=int(input("num2: "))

def add_sub():
    a=num1+num2
    b=abs(num1-num2)
    print(f"addition of {num1} and {num2} is {a}")
    print(f"subtraction of {num1} and {num2} is {b}")

add_sub()