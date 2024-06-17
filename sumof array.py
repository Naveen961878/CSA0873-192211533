sum1=0
array=[]
n=int(input("Enter the no of numbers:"))
for i in range(0,n):
      ele=int(input())
      array.append(ele)
      sum1=sum1+array[i]
print(sum1)
