# A positive integer n is a sum of three cubes
#if n = i3 + j3 + k3 for integers i,j,k such that i ≥ 1, j ≥ 1 and k ≥ 1.
#For instance, 10 is a sum of three cubes because 10 = 13 + 13 + 23, and so is 36 (13 + 23 + 33).
#On the other hand, 4 and 11 are not sums of three cubes
#Write a Python function sum3cubes(n) that takes a positive integer argument and returns True
#if the integer is a sum of three cubes, and False otherwise.


def sum3cubes(n):
  sum=0
  for i in range(1,n):
    for j in range(1,n):
      for k in range(1,n):
        if (i*i*i+j*j*j+k*k*k) == n:
          sum+=1
  if sum>=1: 
    return True
  else:
    return False

