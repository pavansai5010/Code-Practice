'''
to get 2nd largest number form the given input without using built in functions
'''

n=int(input(":"))
elements=input("enter elements separated by space: ")
lst=[]
for i in (elements.split(" ")): # This for loop is to remove the duplicate elements for the given input
    if i not in lst:
        lst.append(i)
print
l=len(lst)
for i in range(l):
    for j in range(i+1,l):
        if lst[i] < lst[j]:
            lst[i],lst[j] = lst[j],lst[i] # this swaps the element if current element is less than 2nd iteration element
print(lst)
print(lst[1]) # this prints the 2nd largest element























































# for i in range(l):
#     for j in range(1,l):
#         if lst[i]>lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
#             print(lst)
        
        