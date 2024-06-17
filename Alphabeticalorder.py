str1=str(input("Enter word : "))
x=sorted(str1)
print("Alphabatical order : ",x)
y=len(x)
ch=""
for i in range(0,y):
    ch=x[i]+ch
print(ch)
