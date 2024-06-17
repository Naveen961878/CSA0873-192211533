def rev(number):
     num,rem=0
num=543
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num/10
print(rev)