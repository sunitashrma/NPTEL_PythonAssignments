# binary search returns index of x in list if present, else -1
def binary_search(l,x,low=None,high=None):
    if low is None:
        low=1
    if high is None:
        high = len(l)-1
    
    
    if high < low:
        return -1 
        
    midpoint=high+low // 2

    if l[midpoint]==x:
        return midpoint 
    elif l[midpoint] > x:
        return binary_search(l,x,low,midpoint-1)
    else:
        return binary_search(l,x,midpoint+1,high)
    
# Print result
 
result= binary_search(l,x)

if result != -1:
    print(f'The index of the element {x} is :',str(result))
else:
    print("elememt is not present in list")

          

    
