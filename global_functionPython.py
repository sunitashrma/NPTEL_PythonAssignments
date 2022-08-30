x=15

def change ():
    global x

x=x+5
print("Value of x inside a function:",x)

change()
print("Value of x outside a function:",x)

# Modifying list variable using global keyword

array = [10,20,30]

def fun():
    global array
    array=[10,40,50]


print("'array'list before executing fun():",array)
fun()

print("'array'list after executing fun():",array)
