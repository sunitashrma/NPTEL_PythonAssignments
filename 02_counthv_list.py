
def counthv(l) :
    hill_count=0
    valley_count=0
    if len(l) >2:
        for i in range (1,len(l)-1):
            if l [ i ] > l [ i-1 ]and l [i ] >l[i +1]:
                hill_count+=1
            elif l[i] <l[i-1] and l[i] < l[i+1]:
                valley_count += 1
        return ([hill_count, valley_count])

    
counthv([1,2,1,2,3,2,1])
[2, 1]
counthv([1,2,3,1])
[1, 0]
counthv([1,2,1,2,3,2,1])
[2, 1]
counthv([3,1,2,3])
[0, 1]
