import numpy as np
r,s=map(int,input().split())
arr=[]
for i in range (r):
	arr+=list(map(int,input().split()))
arr=np.array(arr).reshape(r,s)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
