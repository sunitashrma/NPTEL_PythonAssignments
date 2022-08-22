import time



def prime (a) :
    for j in range (2,a) :
        if a%j == 0:
            return False
        if a== 1:
            return False
        if a<= 0:
            return False
        return True

    
def sumprimes (l):
    sum =0
    for i in range (0,len(l)):
        if prime (l[i]) :
            sum =sum + l[i]
        return (sum)

    
