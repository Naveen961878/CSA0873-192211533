print("hello")
n=543
rem=0
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
    
