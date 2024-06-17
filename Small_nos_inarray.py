n=int(input("Enter the limit:"))
arr=[]
arr1=[]
count=0
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
for i in range(0,n):
    for j in range(0,n):
        if arr[i]>arr[j]:
            count=count+1
    arr1.append(count)
    count=0
print(arr1)
