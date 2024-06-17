str1=str(input("Enter the String:"))
x=sorted(str1)
print(x)
y=len(x)
ch=" "
for i in range(0,y):
    ch=x[i]+ch
print(ch)
