n=int(input("Enter the number:"))
sum=0
rem=0
sum1=0
while n!=0:
    rem=n%10
    sum=sum+rem
    n//=10
sum1=sum
har=float(n)/float(sum1)
print(har)
print("Harshad number")

