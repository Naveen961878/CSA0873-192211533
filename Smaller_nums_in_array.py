n=int(input("Enter the no of numbers:"))
array=[]
count=0
arr1=[]
for i in range(0,n):
    ele=int(input())
    array.append(ele)
print("Original array:",array)
for i in range(0,n):
    for j in range(0,n):
        if(array[i]>array[j]):
            count=count+1
    arr1.append(count)
    count=0
print(arr1)
