n=int(input("How many students:"))
compwinner={}
for a in range(n):
    key=input("Name of the student:")
    value=input("Number s the comptitions won:")
    compwinner[key]=value
print("The dictionary now is:",compwinner)