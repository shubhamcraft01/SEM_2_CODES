import math
n=int(input())
if(n>=1 and n<=9):
	print(f"{n*n}")
elif(n>=10 and n<=99):
	print(f"{math.sqrt(n):.2f}")
elif(n>=100 and n<=999):
	print(f"{math.cbrt(n):.2f}")
else:
	print("Invalid")