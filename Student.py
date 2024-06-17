total=0
agg=0
py=int(input("Enter the Python marks:"))
c=int(input("Enter the C Program marks:"))
mat=int(input("Enter the Mathematics marks:"))
phy=int(input("Enter the Physics marks:"))
total=py+c+mat+phy
agg=total/4
print("Total marks",total)
print("Aggreagte:",agg)
if agg>75:
    print("Distinction")
elif agg<75 & agg>60:
    print("First Class")
elif agg<60 & agg>50:
    print("Second Class")
elif agg<50 & agg>40:
    print("Third Class")
else:
    print("First Class")

