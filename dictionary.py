tec={"shubham":"Math's Teacher","gaurav":"science","mithilesh":"social science"}
tec["Himanshu"]="Computer Engineer"
tec["Himanshu"]="Programer"#updated the entry
print(tec["shubham"])
print(tec.values())
for key in tec:
    print(key,":",tec[key])