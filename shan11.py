def gcd(k,l):
  if k==0:
    return(l)
  else:
    return(gcd(k,l%k))
l,k=map(int,input().split())
p=gcd(l,k)
l=(l*k)//p
print(l)
