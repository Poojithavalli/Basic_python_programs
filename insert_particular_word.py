n=input("enter elements :")
l1=list(map(str,n.split()))
ele=input("enter element that you want to insert in a list: ")
pos=int(input("enter position where you want to insert the word in list :"))
l1.insert(pos,ele)
print(l1)
