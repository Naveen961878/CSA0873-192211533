n=str(input("Enter the String:"))
count=0
count1=0
n=n.lower()
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
        print(i,"is Vowel")
    else:
        count1=count1+1
        print(i,"is consonants")
if(count<count1):
    print("Consonants are Maximum")
elif(count>count1):
    print("Vowels are Max")
else:
    print("Both are equal")
print("No of cosonants:",count1)
print("No of vowels:",count)
