'''
this solution is for the leetcode problem 2363
question:

You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value. 
'''
def merge(items1,items2):
    d=dict()
    for v,w in items1:
        d[v]=w
    for v,w in items2:
        if v in d.keys():
            d[v]=d[v]+w
        else:
            d[v]=w
    
    l = sorted(d.items())
    l = [[k,v] for k,v in l]
    print(l)
    
merge([[1,8],[4,5],[3,8]],[[3,1],[1,5]])