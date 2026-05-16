
import numpy as np 
print("Enter Matrix A:")
matrixa=np.array([list(map(int,input().split()))for i in range (3)])

print("Enter Matrix B:")
matrixb=np.array([list(map(int, input().split()))for i in range (3)])

print("Addition (A + B):")
print(matrixa+matrixb)
print("Subtraction (A - B):")
print(matrixa-matrixb)
print("Element-wise Multiplication (A * B):")
print(matrixa*matrixb)
print("A dot B:")
print(np.dot(matrixa,matrixb))
print("Transpose of A:")
print(matrixa.T)
