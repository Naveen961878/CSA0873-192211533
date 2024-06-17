n=int(input("Enter a number of rows: "))
for i in range(n):
    for j in range((2*n-i)-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
        
