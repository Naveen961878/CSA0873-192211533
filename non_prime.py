A = int(input("enter A value"))
B = int(input("enter B value"))
for num in range(A+1, B + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(num, end=',')
                break
