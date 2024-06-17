n=int(input("Enter the number:"))
arr=[]
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
        ele=i
        arr.append(ele)
print(count)
n1=int(input("Enter the nth number: "))
for i in range(0,n):
    if i==n1-1:
        print(arr[i],"is nth factor")
print(arr)
