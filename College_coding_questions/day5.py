'''
1.A washing machine works on the principle of Fuzzy System, the weight of clothes put 
inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. 
For low level water, the time estimate is 25 minutes, where approximately weight is 
between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is 
between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is 
above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 
0
minutes. 
If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all 
negative weights, the output is “INVALID INPUT”.
Sample Input-1: 2000
Sample Output-1: Time Estimated: 25 minutes
Input should be in the form of integer value. 
Output must have the following format: Time Estimated: NN Minutes

'''
weight = int(input(":"))
def washing_machine(weight):
    
    if 0==weight  :
        print("Time estimated : 0 Minutes")
    elif weight<0:
        print("Invalid Input")
    elif 0<weight<=2000:
        print("Time estimated : 25 Minutes")
    elif 2000<weight<=4000:
        print("Time estimated : 35 Minutes")
    elif 4001<weight<=7000:
        print("Time estimated : 45 Minutes")
    else:
        print("OVERLOADED")
        
print(washing_machine(weight))
        