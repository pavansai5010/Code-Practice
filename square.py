# get squares between start and end numbers
start = int(input("Enter yout starting number: "))
end = int(input("Enter yout ending number: "))
def get_sqrs(start,end):
    print(f"square between {start} and {end} numbers")
    while start<=end:
        print(f"{start} {start**2}")
        start+=1
get_sqrs(start,end)