n=143
sum=0
rem=0
sum1=0
rem1=0
while n!=0:
    rem=n%10
    sum=sum+rem
    n//10
while sum!=0:
    if sum>=10:
        rem1=rem1%10
        sum1=sum1+rem1
        sum//=10
    else:
        sum1=sum
print(sum1)
