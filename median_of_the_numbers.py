# The median of three numbers x,y,z is the second number in the sequence
# when the three numbers are sorted in ascending or descending order.  

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x


  if x>y:
      if x<z:
        mymedian=x
      elif y>z:
        mymedian=y
      else:
        mymedian=z
  else:
      if x>z:
        mymedian=x
      elif y<z:
        mymedian=y
      else:
        mymedian=z
  return mymedian
# Test samples

# print(median3(1,2,3))
# print(median3(3,1,2))
