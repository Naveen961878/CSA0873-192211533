n=int(input("Enter the limit:"))
arr=[]
arr2=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
x=int(input("Enter the no to Search:"))
for i in range(0,n):
    if arr[i]==x:
        arr2.append(i)
print(arr2)
