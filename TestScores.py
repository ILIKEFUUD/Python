"""
Rahul Shah
Use for loop to read in test scores
print total and average

TestScores.py
PD3
"""

total = 0

for i in range(0,5):
    total += int(input("Enter a test score: "))

print("Total: ", total)
print("average: ", total/5)
