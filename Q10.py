num = int(input("enter a number: "))
product = 1
no = num
def product_of_digits(num):
    while no != 0 :
        r = no%10
        product = product * r
        no = no // 10
