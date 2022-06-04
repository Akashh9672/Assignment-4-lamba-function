from difflib import SequenceMatcher


size=int(input("Enter the size of list:"))
lst=[]

for i in range(size):
    number=int(input("enter any no:"))
    lst.append(number)
print("Your list:",lst)
square=list(map(lambda x:x**2 , lst))
print("Your answer list of squares:", square)