def myfunc3(mylist):
    print("\t Inside called function")
    print("\t List recived:",mylist)
    mylist.append(2)#add 2 in the list
    mylist.extend([5,1])#add 5,1 in the list
    print("\t List after adding some elemnts:",mylist)
    mylist.remove(5)#remove 5 in the list
    print("\t List within called function, after all changes:",mylist)
    return
list1=[1]
print("List before function call",list1)
myfunc3(list1)#a func which can add and deleate elements in the list
print("\t List after function call:",list1)#intended by myfunc3
