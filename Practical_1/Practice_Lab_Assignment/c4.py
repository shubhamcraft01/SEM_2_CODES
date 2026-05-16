n=int(input())
x=0
while n>0:
	x=x*10
	i=n%10
	n=n//10
	x=x+i
print(x)