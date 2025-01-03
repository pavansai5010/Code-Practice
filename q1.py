start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# even numbers
def  get_even(start,end):
    print(f"even numbers between {start} and {end}:")
    while start <= end:
        if start % 2 == 0:
            print(start)
        start +=1

#odd numbers
def get_odd(start,end):
    print(f"Odd numbers between {start} and {end}:")
    while start <=end:
        if start %2 ==1:
            print(start)
        start+=1

get_even(start,end)
get_odd(start,end)
