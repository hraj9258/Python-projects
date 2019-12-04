lst=["red","blue","green"]
lst2=["black"]
#lst[1]=11 replaces the 1st element i.e.blue with 11
#del lst[1:3]
lst.append("yellow")
seq=lst.index("blue")
extd=lst.extend(lst2)
insrt=lst.insert(2,"green")
pop=lst.pop(1)
remove=lst.remove("red")
count=lst.count("green")
#clear=lst.clear()
print("printing the indexing value of blue:",seq)
print("printing the list:",lst,"Hear black is extended","Red is removed")
#print("Printing the extended list:",extd)
print("printing the poped character:",pop)
print(count)
#print(remove)
#print(app)