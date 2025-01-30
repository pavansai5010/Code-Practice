string = input(":")
def palindrome(string):
    s=""
    l=[]
    for i in string:
        if i.isalpha():
            s=s+(i.lower())
    print(s)
    for i in s:
        l.append(i)
    if "".join(l) == s:
        return True
    else:
        return False
    
print(palindrome(string))