n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
for i in range(n,m+1):
    for j in range(2,i):
        if i==j:
            continue
        elif i%j==0:
            print(i)
            break
