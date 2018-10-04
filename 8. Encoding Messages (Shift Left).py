#Name: Hashir Khan
#Date: September 24, 2018
#This program shifts every letter to the left
x = input("Enter your message: ")
y = ""
for i in x:
    if ord(i)==65:
        z = "Z"
    elif ord(i)==97:
        z = "z"
    else:
        z = chr(ord(i)-1)
    y+=z
print(y)
