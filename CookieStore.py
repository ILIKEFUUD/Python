"""
Rahul Shah
CookieStore.py

Simulates a cookie store
print out cheapest way that user can buy desired amount of cookies
advise them to buy a box of 12 cookies since it would be same or cheaper
assume user may buy minimum of one cookie and maximum of 12 cookies
"""

numCookies = input("How many cookies do you desire? (Min:  1, Max: 12")

num = int(numCookies)

price = num * .25

if(price >= 2.5):
    print("You should buy a box of 12 cookies, expect to pay: $2.50")
else:
    print("You should buy it per cookie. Expect to pay: $" + str(price))
