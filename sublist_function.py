# A sublist of a list is a segment consisting of contiguous values

def sublist(l1,l2):
    f = 0
    for i in range (len(l2)-len(l1)):
        if l2 [i : len(l1)] == l1 and len(l1) != 1:
            f =2
        elif len(l1) == 1 and l1[0] in l2 :
            f =2
    return (f==2)
# Test Samples

# print (sublist([2,2,4],[2,2,3,4,5]))
# print (sublist([2,2,3],[2,2,3,4]))



    
