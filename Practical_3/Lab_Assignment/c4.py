import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print("Element-wise Sum:", *(A + B))
print("Element-wise Difference:", *(A - B))
print("Element-wise Product:", *(A * B))

print("Mean of A:", np.mean(A))
print("Median of A:", np.median(A))
print("Standard Deviation of A:", np.std(A))

print("Bitwise AND:", *(A & B))
print("Bitwise OR:", *(A | B))
print("Bitwise XOR:", *(A ^ B))