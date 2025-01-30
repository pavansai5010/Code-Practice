'''
to print the pattern of numbers:
'''
n=int(input("Enter number of numbers to be printed: "))
for i in range(1,n+1):
    print(f"{i}  {(n+1)-i}")
    