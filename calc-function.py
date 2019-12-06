print("List of opreations:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
inp=input("Please Enter What you Want to do:")
def calsum(x,y):
    if inp=="1":
        s=x+y
        return s
    elif inp=="2":
        s=x-y
        return s
    elif inp=="3":
        s=x*y
        return s
    elif inp=="4":
        s=x/y
        return s
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
x=calsum(num1,num2)
print("Resulting number is:",x)