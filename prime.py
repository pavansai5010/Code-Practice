start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print(f"Prime numbers between {start} and {end}: ")

# prime numbers
def is_prime(number):
    
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True
    
current = start

while current <= end:
    if is_prime(current):
        print(current)
    current += 1