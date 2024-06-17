n=int(input("Enter the last limit:"))
sum=0
fact=1
arr=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        fact=fact*j
        ele=fact
    arr.append(ele)
    fact=1
for i in range(n):
    sum=sum+arr[i]
print(sum)
