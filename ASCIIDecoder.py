"""
Rahul Shah

Decodes a message from decimal values
representing ASCII values into words

"""


size = int(input("How long is your message?"))

s = ""

for i in range(0,size):
    num = int(input("Enter ASCII value:"))
    s+= str(chr(num))

print("Your message is: " ,s)
