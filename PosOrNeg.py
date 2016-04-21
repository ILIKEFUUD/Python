"""
Rahul Shah
PosOrNeg.py
12/8/15
Reads in number tells if its zero positive or negative
"""

isDone = False

while(not isDone):
    try:
        num = input("Enter a num: ")
        if(int(num) == 0):
            print("It's zero")
        elif(int(num) < 0):
            print("It's a negative")
        else:
            print("It's a positive")
    
    except:
        isDone = True
        print("terminated")
    
