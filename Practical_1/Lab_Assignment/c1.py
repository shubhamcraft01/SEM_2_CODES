# Input number of courses
n = int(input())

# Input marks
marks = list(map(int, input().split()))

# Check fail condition
fail = False
for i in range(len(marks)):
	if marks[i] < 40:
		fail = True

if fail:
	print("Fail")
else:
	total = 0
	for i in range(len(marks)):
		total = total + marks[i]

	percentage = total / n

	print(f"Aggregate Percentage: {percentage:.2f}")

	if percentage > 75:
		print("Grade: Distinction")
	elif percentage >= 60:
		print("Grade: First Division")
	elif percentage >= 50:
		print("Grade: Second Division")
	elif percentage >= 40:
		print("Grade: Third Division")