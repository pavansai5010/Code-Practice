# sum of first 10 even numbers

def SOEN():
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    sum = 0
    while start<=end:
        if start % 2 == 0:
            sum = sum + start 
        start+=1
    print(sum)

SOEN()