n=int(input("Enter the year:"))
rem=0
if n%4==0:
      print("Leap_Year")
else:
    rem=n%10
    print(4-rem,"years for leap years")
    print("It is not Leap Year")
