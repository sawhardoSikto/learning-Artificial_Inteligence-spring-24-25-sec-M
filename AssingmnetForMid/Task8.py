#task8
people={
    "sikto":21,
    "bikash":20,
    "panic":22
     
}
print (people)
f=input("enter name to find the age ")
if f in people:
    print(f,"'s age is",people[f]);
else:
    print("the name does not found")
