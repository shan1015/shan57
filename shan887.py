k,m=map(int,input().split())
l=[]
k=[]
sum=1
for i in range(1,k+1):
	if k%i==0:
		l.append(i)
for i in range(1,m+1):
	if m%i==0:
		l.append(i)
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if l[i]==l[j]:
			sum=sum*l[i]
			
print(sum)
