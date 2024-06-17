n=int(input("Enter trhe number:"))
c=1
for i in range(2,n+1):
    if n%i==0:
        c=c+1
        print('Factors are',i)
print("The number of factors for",n,"is",c)

