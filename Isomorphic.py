str1=str(input("Enter string 1 : "))
str2=str(input("Enter string 2 : "))
x=len(str1)
y=len(str2)
ch1=""
ch2=""
ch3=""
iso=1
for i in range(0,x):
    #ch1=str1[i]
    for i in range(0,y):
        #ch2=str2[i]
        ch2=str1[1]+str2[1]
        ch3=str1[2]+str2[2]
        if(ch2==ch3):
            iso=iso+1
if(iso>1):
    print("isomarphic")
else:
    print("not isomarphic")
