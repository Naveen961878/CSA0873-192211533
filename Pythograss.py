n=int(input("Enter the number:"))
x=0
y=0
z=0
for i in range(1,n+1):
    x=i**2
    a=i
    for j in range(1,n+1):
        y==j**2
        b=j
        for k in  range(1,n+1):
            z=k**2
            c=k
            if(x+y==z):
                print(a,b,c)
