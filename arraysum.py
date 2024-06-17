print("Press -1 for Exit the Array")
arr=[]
c1=1
c2=1
n=100
x=0
avg_pos=0
avg_neg=0
for i in range(0,n):
    ele=int(input("Enter the number:"))
    arr.append(ele)
    x=x+1
    if arr[i]==-1:
        break
sum_pos=0
sum_neg=0
for i in range(0,x):
    if arr[i]>=0:
        sum_pos=sum_pos+arr[i]
        c1=c1+1
    else:
        sum_neg=sum_neg+arr[i]
        c2=c2+1
avg_pos=float(sum_pos)/(float(c1)-1)
avg_neg=float(sum_neg)/(float(c2)-1)
print("Positive numbers average is ",float(avg_pos))
print("Neagative numbers average is ",float(avg_neg))
