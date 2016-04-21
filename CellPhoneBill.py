"""
Rahul Shah
Period 2
CellPhoneBill.py
Determines best plan for user's minutes
"""
price = 0
plan = ""
minutes = input("Enter number of minutes: ")
m = float(minutes)
if(m == 0):
    price = 0
    plan = "None... You don't need one."
elif(m <= 428):
    if(m >= 400):
        price = 30 + .35*(m-400)
        plan = "Basic Talk"
    else:
        price = 30
        plan = "Basic Talk"
elif(m <= 200/.3):
    if(m >= 600):
        price = 40 + .30 * (m-600)
        plan = "Standard Talk"
    else:
        price = 40
        plan = "Standard Talk"
else:
    price = 60
    plan = "Unlimited Talk"

print("The best plan for you is : " , plan)
print("Expect to pay: $", price)
