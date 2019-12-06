def interest(principal,time=2,rate=0.10):
    return principal*rate*time

#__main__
prin=float(input("Please Enter the Principal Amount:"))
print("Simple interest with default ROI and time Value is:","Rs.",interest(prin))
roi=float(input("Enter Rate of Intrest(ROI):"))
time=int(input("Enter time in years:"))
print("Simpel interest with your provided ROI and time value is")
si2=interest(prin,time,roi/100)
print("Rs.",si2)
