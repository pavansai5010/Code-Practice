# series 10,20,30,...
start = int(input("Enter starting number: "))
end = int(input("Enter end number: "))
def get_series(start,end):
    if start>end:
        while start>end:
            print(start*10)
            start-=1
    else:
        while start<=end:
            print(start*10)
            start+=1           
            
get_series(start,end)