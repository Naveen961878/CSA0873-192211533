n=int(input("Enter the numbers:"))
arr=[]
arr1=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
for i in range(0,n):
    if arr[i]%3==0:
        x="Fizz"
        arr1.append(x)
    elif arr[i]%5==0:
        x="Buzz"
        arr1.append(x)
    else:
        arr1.append(arr[i])
print(arr1)z
        
        
