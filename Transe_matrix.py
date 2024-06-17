n=[[4,6,7,8],
   [3,7,2,7],
   [7,3,7,5]]
x=[[0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0]]
s=len(n)
for i in range(0,s):
    for j in range(0,len(x)):
        x[j][i]=n[i][j]
for i in range(0,s):
    for j in range(len(x)):
        print(x[j])
    print("\n")
    
