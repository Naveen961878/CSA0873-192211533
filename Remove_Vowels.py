str1=str(input("Enter string : "))
x=len(str1)
ch=""
ch1=""
for i in range(0,x):
    ch=str1[i]
    if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U'):
        continue
    else:
        ch1=ch1+ch
print(ch1)
