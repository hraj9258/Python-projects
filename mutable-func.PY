def myfunc2(mylist):
    print("\n\t Inside called Function now")
    print("\t List recived:",mylist)
    mylist[0]+=2
    print("\t List within called function, after changes:",mylist)

list1=[1]
print("List before function call:",list1)
myfunc2(list1)
print("\nList after function call:",list1)
#making changes in place.