n=input("enter elements to calculate sum:")
l1=list(map(int,n.split()))
sum=0
for i in l1:
    sum=sum+i
print("sum of elements in the list is",sum)
