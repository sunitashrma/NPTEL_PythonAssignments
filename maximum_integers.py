# find maximum integers out of 4 integers

def max4(w,x,y,z):

    if w>=x and w>=y and w>=z:
      maximum = w
    elif y>=x and y>=w and y>=z:
        maximum=y
    elif x>=w and x>=y and x>=z:
        maximum=x

    else:
        maximum=z

    return maximum


print(max4(12,10,8,5))
