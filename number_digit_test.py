num=int(input("Enter a number  (0...999) : "))
if num<0:
    print('Invalid Entry. Valid Range is 0 to 999')
elif num<10:
    print("Single Degit Number is enterd")
elif num<100:
    print("Two degit number isenterd")
elif num<=999:
    print("Three digit njumber is enterd")
else:
    print("Invalidentry. Valid range is 0 to 999.")