
def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)


intreverse(568)
765
intreverse(656)
656
intreverse(7896)
6987
