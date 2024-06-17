n=int(input("Enter the number:"))
arr=[]
arr1=[]
for i in range(0,n):
    ele=int(input("Enter the Element:"))
    arr.append(ele)
print("Original",arr)
arr=sorted(arr)
arr1=arr
print("Sorted:",arr)
k=int(input("Enter th enumber to insert:"))
pos=int(input("Enter the index value:"))
for i in range(0,n):
    if i==pos:
        arr[i-1]=k
print(arr1)
print(arr)
