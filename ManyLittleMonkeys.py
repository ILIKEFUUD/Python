"""
Rahul Shah
Period 3
1/7/16
ManyLittleMonkeys.py
Prints out the nursery rhyme using while loops
"""

m = input("How many monkeys were irresponsibly jumping on the bed? ")
monkeys = int(m)
while(monkeys > 0):
    if(monkeys == 1):
        print("1 little monkey jumping on the bed")
    else:
        print(monkeys, " little monkeys jumping on the bed.")
    print("One fell off and bumped his head.")
    print("Momma called the doctor and the doctor said: ")
    print("No more monkeys jumping on the bed!")
    print()
    monkeys-=1
    

