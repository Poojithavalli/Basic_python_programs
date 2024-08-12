def largest_of_three():
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    n3=int(input("enter third number:"))
    if n1>n2 and n1>n3:
        print(f"{n1} is larger number")
    elif n2>n3:
        print(f"{n2} is larger number")
    else:
        print(f"{n3} is larger number")
largest_of_three()
