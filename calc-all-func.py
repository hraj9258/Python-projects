def cal(x,y):
    return x+y,x-y,x*y,x/y,x%y
num1=int(input("Please Enter first number:"))
num2=int(input("please enter second number:"))
add,sub,mult,div,mod=cal(num1,num2)
print("Addititon of two numbers:",add)
print("Subtraction of two numbers:",sub)
print("Multiplication of two numbers:",mult)
print("Divion of two numbers:",div)
print("Modulo of two numbers:",mod)