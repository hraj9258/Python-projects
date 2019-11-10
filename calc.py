print("What you want to do ?")
print("+","-","*","/")
x=input("Please enter one of the above oprater.")
if x=="+": 
    num1=int(input("Please enter first Number."))
    num2=int(input("Please enter second Number."))
    res=num1+num2
    print(res)
if x=="-":
    num1=int(input("Please enter first Number."))
    num2=int(input("Please enter second Number."))
    print(num1-num2)
if x=="*":
    num1=int(input("Please enter first Number."))
    num2=int(input("Please enter second Number."))
    print(num1*num2)
if x=="/":
    num1=int(input("Please enter first Number."))
    num2=int(input("Please enter second Number."))
    print(num1/num2)
else:
    print("Please enter your choice Again")