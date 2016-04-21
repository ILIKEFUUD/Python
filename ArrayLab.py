"""
Rahul Shah
Pd 6
ArrayLab.py
- Constructed an array of 50 integers

- Initialized the array of 50 integers with the numbers 1 to 50.

- Printed out the numbers 1 to 50 separated by commas on the same line.


"""


#python actually uses lists, which are basically arrays

nums = []

#populate array
for i in range(1,51):
    nums.append(i)

#print array
for i in nums:
    print(i,end=',')#apparently this is how you print on one line, seperated by a comma
    #python 3 is weird
