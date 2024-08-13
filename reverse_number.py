n=int(input("enter number that you want to reverse:"))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print("The reverse of a number is ",s)
