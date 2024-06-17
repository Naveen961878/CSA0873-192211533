str1=str(input("Enter the string:"))
str2=str(input("Enter the character to search:"))
x=len(str1)
y=len(str2)
for i in range(0,x):
    ch=str1[i]
    for j in range(0,y):
        ch1=str2[j]
    if ch==ch1:
        print(ch,"Character at index",i)
    
