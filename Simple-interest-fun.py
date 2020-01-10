def interest(principal,time=2,rate=0.10):
    return principal*rate*time

#__main__
principal=float(input("Please Enter the Principal Amount:"))
print("Simple interest with default ROI(0.10) and time(2) Value is:","Rs.",interest(principal/100))
roi=float(input("Enter Rate of Intrest(ROI):"))
time=int(input("Enter time in years:"))
print("Simpel interest with your provided ROI and time value is")
si2=interest(principal,time,roi/100)
print("Rs.",si2)
