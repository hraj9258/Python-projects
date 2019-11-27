print("What you want to do:")
print("1.Captilize the first character of the enterd sentance.")
print("2.Capatilize the enterd sentance.")
print("3.Lowercase the enterd sentance.")
opt=str(input("Please enter the desired option:"))
if opt =="1":
    x=str(input("Enter the sentance to captilize the first letter:"))
    y=x.capitalize()   
    print(y)
elif opt=="2":
    x=str(input("Enter the sentence to captilize:"))
    y=x.upper()   
    print(y)
elif opt=="3":
    x=str(input("Enter the sentence to lowercase it:"))
    y=x.lower()
    print(y)