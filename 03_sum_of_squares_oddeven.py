

def sumsquare (l):
    odd=0
    even=0
    for a in l:
        if a%2 == 0:
            even= even + a**2
        else:
            odd = odd + a**2
    l= [odd, even]
    return (l)

