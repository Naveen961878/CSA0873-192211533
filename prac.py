import datetime
a=int(input("Enter the Year:"))
b=int(input("Enter the Month:"))
c=int(input("Enter the Date:"))
x=datetime.date(a,b,c)
y=x.strfdatetime("%A")
print(y)
