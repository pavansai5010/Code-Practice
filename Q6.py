def natural_sum():
    start = int(input("Enter the start value: "))
    end=int(input("Enter the end value: "))
    sum = 0
    while start<=end:
        sum = sum+start
        start = start+1
    print(sum)

natural_sum()