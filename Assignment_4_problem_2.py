size=int(input("Enter the size of list:"))
lst=[]

for i in range(size):
    number=int(input("enter any no:"))
    lst.append(number)
print("Your list:",lst)
tripple=list(map(lambda x:x*3 , lst))
print("Your answer list of tripple og every number:",tripple)