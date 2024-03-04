#A lesson to demonstrate the concept of condition statements in python.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("The sum of ",a ,"and" ,b, "is",c)
if(c>a):
    print(c,"is greater than",a)
else:
    print(c,"is less than ",a)
