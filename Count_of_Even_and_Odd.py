a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
c=int(input("Enter your third number"))
d=int(input("Enter your fourth and last number"))
list=[]
list.append(a)
list.append(b)
list.append(c)
list.append(d)
i=0
Even=0
Odd=0
for i in list:
    if(i%2==0):
        Even=Even+1
    else:
        Odd=Odd+1

if(Even==1):
    print("There is 1 even number")
else:
    print("There are ", Even, "even numbers")


if(Odd==1):
    print("There is 1 odd number")
else:
    print("There are ", Odd, "odd numbers")
