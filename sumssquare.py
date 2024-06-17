def sumsquare(n):
    x=y
    arr=[]
    odd=0
    even=0
    for i in range(0,x):
        ele=int(input('Enter Number : '))
        arr.append(ele)
    for i in range(0,x):
        if(arr[i]%2==0):
            even=even+arr[i]**2
        else:
            odd=odd+arr[i]**2
    arr1=[odd,even]
    print(arr1)

y=int(input("Enter numbers of elements : "))
sumsquare(y)
