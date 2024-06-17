n=int(input("Enter the n digit number"))
sum=0
sum1=0
rem=0
rev=0
while n!=0:
    rem=n%10
    rev=rev+rem
    n//=10
sum=rev
while sum>=10:
    sum%10
    sum1=sum1+sum
    sum//10    
#print("Sum of digits is ",rev)
print("Sum of digits is ",sum)
