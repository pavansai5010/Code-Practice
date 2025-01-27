n=int(input(":"))
elements=input("enter elements separated by space: ")
lst=[]
for i in (elements.split(" ")):
    if i not in lst:
        lst.append(i)
print
l=len(lst)
for i in range(l):
    for j in range(i+1,l):
        if lst[i] < lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
print(lst)
print(lst[1])























































# for i in range(l):
#     for j in range(1,l):
#         if lst[i]>lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
#             print(lst)
        
        