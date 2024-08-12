length=int(input("enter length of the fibonacci series :"))
n1,n2=0,1
print(n1)
print(n2)
for i in range(length-2):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    
