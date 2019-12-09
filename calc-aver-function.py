def calcsum(a,b,c):
    s=a+b+c
    return s

def average(x,y,z):
    sm=calcsum(x,y,z)
    return sm/3

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
print("Average of these number is:",average(num1,num2,num3))