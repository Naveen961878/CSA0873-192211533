n=7
x=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if x==sum:
    print("Perfect")
else:
    print("Not perfect")
