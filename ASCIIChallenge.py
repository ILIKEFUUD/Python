"""
Rahul Shah
ASCII name challenge
PD 6
4/19/16
asks user for name, displays ascii values on one line
"""


name = input("ENTER A NAME, HUMAN:")

string = ""

for i in name:
    string += (str)(ord(i)) + " "

 
print(string)
