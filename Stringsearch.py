str1=str(input("Enter first string : "))
str2=str(input("Enter second string : "))
x=len(str1)
y=len(str2)
z=0
for i in range(0,x):
    ch1=str1[i]
    for j in range(0,y):
        ch2=str2[j]
        if(i==j and ch1==ch2):
            z=z+1
print(z)
