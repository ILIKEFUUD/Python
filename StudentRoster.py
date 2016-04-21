"""
Rahul Shah
StudentRoster.py

Sell PD 6

3/18/16

makes an array of students and prints out
their names
"""
students = []

num = int(input("How many students are in the class?: "))

for i in range(0,num):
    print("Enter name of student", i + 1)
    students.append(input("name: ")) #must use append


for i in range(0,num):
    print(students[i])
