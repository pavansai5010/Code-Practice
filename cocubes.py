'''
This programs appends the underscore in the string to the end of the  string without changing the order of normal characters in the string 
'''
string = input("Enter a string: ")
s=""
l=[]
c=0
for i in string:  # I am converting the string into list for better understanding 
    if i == '_':
        c+=1      # To know the 5
    else:
        l.append(i)  
print(l)
print(c)
for i in l:
    s+=i
print(s+(c*('_')))
    
