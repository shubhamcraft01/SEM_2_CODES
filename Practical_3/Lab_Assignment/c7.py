import numpy as np

a = np.loadtxt("Sample.csv", delimiter=",", skiprows=1)

print("All student Details:\n", a)

print("Total Students:", len(a))

print("All Student Roll Nos", a[:, 0])

print("Subject 1 Marks", a[:, 1])

print("Min marks in Subject 2", min(a[:, 2]))

print("Max marks in Subject 3", max(a[:, 3]))

print("All subject marks:", a[:, 1:])

print("Total Marks", a[:, 1] + a[:, 2] + a[:, 3])

print(np.round((a[:, 1] + a[:, 2] + a[:, 3]) / 3, 1))

print("Average Marks of each subject", np.round(np.mean(a[:, 1:], axis=0), 1))

print("Average Marks of S1 and S2", 
      np.round([np.mean(a[:, 1]), np.mean(a[:, 2])], 1))

print("Average Marks of S1 and S3", 
      np.round([np.mean(a[:, 1]), np.mean(a[:, 3])], 1))

print("Roll no who got maximum marks in Subject 3", 
      a[np.argmax(a[:, 3]), 0])

print("Roll no who got minimum marks in Subject 2", 
      a[np.argmin(a[:, 2]), 0])

print("Roll no who got 24 marks in Subject 2", 
      a[a[:, 2] == 24, 0:1])

print("Count of students who got marks in Subject 1 < 40", 
      np.sum(a[:, 1] < 40))

print("Count of students who got marks in Subject 2 > 90:", 
      np.sum(a[:, 2] > 90))

print("Count of students in each subject who got marks >= 90:", 
      np.sum(a[:, 1:] >= 90, axis=0))

print("Roll no:", a[:, 0])

print("Count of subjects in which student got marks >= 90:", 
      np.sum(a[:, 1:] >= 90, axis=1).astype(int))

print(np.sort(a[:, 1]))

print(a[(a[:, 1] >= 50) & (a[:, 1] <= 90)])

print(a)

print(np.where(a[:, 1] == 79))