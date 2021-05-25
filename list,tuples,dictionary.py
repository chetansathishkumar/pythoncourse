#LISTS
#ordered, changeable and allow duplicates
lis =[2,2002,"sathish"]
print(lis)
print(len(lis))
print(lis[1])
print(lis[-2:])

lis[2]="chetan"
print(lis)
lis.append("apple")
print(lis)
lis.remove("chetan")
print(lis)
lis.insert(0,"car")
print(lis)



#TUPLES
#ordered , unchangable and allow duplicates

tuple =("chetan","sathish",3,2002)
print(len(tuple))
print(tuple)
print(type(tuple))
print(tuple[2])








#Dictionary
#Unordered , changable and DO NOT allow duplicates

d1 = {
    'name' : "chetan",
    'age' : "18" ,
    'laptop' : "lenovo",
    'model' : "ideapad 305"
}
print(d1)
print(len(d1))
