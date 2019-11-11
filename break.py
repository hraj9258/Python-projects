a=b=c=0#still dont know why it is hear
for i in range (1,11):
    a=int(input("Enter first number :"))
    b=int(input("Enter second number"))
    if b==0:
        print("Division by zero error ! Aborting!")
        break
    else:
        c=a/b
        print("Quotient= ",c)
print("Program over")