# A positive integer n is said to be perfect
# if the sum of the factors of n, other than n itself, add upto n
# example: 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6

def perfect (n):
     sum=0
     for i in range (1,n):
         if n%i == 0:
             sum+= i
     return (sum == n)

# Test samples

# print (perfect(28))
# print(perfect(8))

# print(perfect(6))
