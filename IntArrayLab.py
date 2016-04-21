"""
Rahul Shah
Pd 6
initializes an array called myArray
of 10 integers, each integer is
an increment of 10
display the array and the length

IntArrayLab.py
"""

#initialize array
myArray = []

#populate array
for i in range(0,10):myArray.append(10 * (i + 1))

#print array
for t in range (0,10):print("index ",t," of myArray is: ", myArray[t])
print("length of myArray is: ", len(myArray))

