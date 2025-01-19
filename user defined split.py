string = input("enter a string: ")
delimiter = input("enter a valid separator: ")
res=[]
current=""
if delimiter not in string:
    print("ERROR: Enter a valid separator!!")
else:
    for char in string:
        if char == delimiter:
            res.append(current)
            current=""
        else:
            current=current+char
    res.append(current)
    
print(res)
            
    
