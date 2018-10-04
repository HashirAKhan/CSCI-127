#Name: Hashir Khan
#Date: October 3rd, 2018
#This assignment prints a pyrimid using a message
x = input("enter prompt: ")
ls = len(x)
for i in range(0,ls):
    print(x[0:i])
for i in range(0,ls):
    print(x[i:ls])
print("thanks for using this!")
