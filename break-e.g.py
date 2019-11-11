#x=y=0
#x=int(input("Please enter first number:"))
#y=int(input("Please enter second number:"))
for y in range(0,1):
    x=int(input("Please enter first number:"))
    y=int(input("Please enter second number:"))
    if y == 0:
        print("Devision by zero error!")
        break
    if y == 1:
        print("Devision of",x,"by 1","is",x)
    else:
        print("Division of",x,"and",y,"is",x/y)
print("Program over!")