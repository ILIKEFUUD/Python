"""
Rahul Shah
OhmsLawCalculator.py
Calculates resistance or voltage or current
2/17/16
"""

str = input("What value would you like to calculate: \n1. Voltage \n2. Current \n3. Resistance \n")
if(int(str) ==1): #if Voltage
    i = input("Enter Current: ")
    r = input("Enter Resistance: ")
    print("The voltage is: " ,float(i)*float(r), "Volts")
elif(int(str) == 2): #if Current
    v = input("Enter Voltage: ")
    r = input("Enter Resistance: ")
    print("The current is: " ,float(v)/float(r), "Amps")
else: #if Resistance
    v = input("Enter Voltage: ")
    i = input("Enter Current: ")
    print("The resistance is: " , float(v)/float(i), "Ohms")
