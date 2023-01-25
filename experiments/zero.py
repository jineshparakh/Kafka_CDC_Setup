import os

doc ={
    "id":1,
    "name":"name_i"
}
values=[]
for i in range(5):
    
    doc["name"]="name_"+str(i)
    print(doc)
    values.append(doc.copy())

print(values)
