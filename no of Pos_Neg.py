y=int(input("Enter no of elements : "))
arr=[]
neg=0
pos=0
for i in range(0,y):
    ele=int(input())
    arr.append(ele)
for i in range(0,y):
    if(arr[i]<0):
        neg=neg+1
    else:
        pos=pos+1
print("negitive no's are : ",neg)
print("positive no's are : ",pos)
