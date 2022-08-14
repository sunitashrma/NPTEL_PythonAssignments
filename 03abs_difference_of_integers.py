


def contracting (l):
    a=0
    for i in range (1,len(l)) :
        if a >= abs (l[i]- l[i-1]) :
            return True
        a=abs(l[i]- l[i-1])
    else:
        return False

 
