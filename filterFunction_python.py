# filter function examples
#1.
def fun(variable):
    letters=['a','e','i','o','u']
    if variable in letters:
       return True
    else:
        return False


sequence=['g','l','p','i','k','u']
 # using filter function

filtered=filter(fun,sequence)
print("The filtered letters are:")
for s in filtered:
    print(s)

#2.

ages = [5,10,12,15,20,24,30]

def my_fun(x):
    if x <18:
        return False
    else:
        return True
adults=filter(my_fun,ages)
for x in adults:
  print(x)


  

#3
