arr=[]
x=int(input())
for i in range(0,x):
    ele=int(input())
    arr.append(ele)
for i in range(0,int(x/2)):
    temp=arr[i]
    arr[i]=arr[x-i-1]
    arr[x-i-1]=temp
for i in range(0,x):
    print(arr[i])
