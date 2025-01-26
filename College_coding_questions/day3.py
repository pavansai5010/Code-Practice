'''
--This program is made with the reference to the video "https://youtu.be/u-Ptydkqh7E?si=HxIwIH74qz6myzrA"--
Program to calculate the average of the list of heights.

I did't used any built in function like len(),sum() or avg().
'''

h = input("enter heights separated by space: ")
def AVG(h):
    
    lst=h.split(" ")# this will split the string where ever it finds space in the given string
    s=0
    c=0 
    for i in lst:
        s+=int(i)
        c+=1 # To know the no.of heights were given
    return (s//c)

print(AVG(h))