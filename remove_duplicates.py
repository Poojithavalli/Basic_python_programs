n=input("enter elements :")
l1=list(map(int,n.split()))
print("elements in the list are",l1)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print("list elements without duplicates are",l2)
