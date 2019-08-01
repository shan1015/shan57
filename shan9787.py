a=input()
m=list(a)
s=""
l=""
for i in range(0,len(m)):
	if i%2==0:
		s=s+str(m[i])+""
	if i%2==1:
		l=l+str(m[i])+""
print(s.strip(),end=" ")
print(l.strip())
#i
