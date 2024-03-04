#A lesson to demonstrate the concept of condition statements in python.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("The sum of ",a ,"and" ,b, "is",c)
if(c>a):
    print(c,"is greater than",a)
elif(c==a):
    print(c, "is equal to",a)
    if(c==b):
        print("C is equals to",b)
    elif(c==c):
     print("C is  equals to",c)
    else:
        print(C, "is other than any of here")

else:
    print(c,"is less than ",a)
