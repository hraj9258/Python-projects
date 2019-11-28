line=input("Enter a line:")
lowercount=uppercount=0
digitcount=alphacount=digitspace=0
for a in line:
    if a.islower():
        lowercount +=1
    elif a.isupper():
        uppercount +=1
    elif a.isdigit():
        digitcount +=1
    elif a.isalpha():
        alphacount +=1
    elif a.isspace():
        digitspace +=1

print("Number of upper case letter:",uppercount)
print("Number of lowercase letters:",lowercount)
print("Number of alphabet:",alphacount)
print("Number of digits:",digitcount)
print("Number of spaces:",digitspace)

