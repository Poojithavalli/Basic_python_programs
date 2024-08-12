def prime():
    n=int(input("enter a number to check whether it is prime or not :"))
    if n==1:
        print(f"{n} is not a prime")
    elif n>1:
        for i in range(2,n):
            if n%i==0:
                print(f"{n} is not a prime number")
                break
        else:
                print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
prime()
