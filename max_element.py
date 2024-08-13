n=input("enter elements: ")
l=list(map(int,n.split()))
print("the elements in the list are",l)
max=0
for i in l:
    if max<i:
        max=i
print(f"The maximum element in the list is {max}")
       
