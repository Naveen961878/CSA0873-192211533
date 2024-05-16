def is_perfect_number(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n
number = 6
if is_perfect_number(number):
    print(f"Given Number: {number}")
    print("It's a Perfect Number")
else:
    print(f"Given Number: {number}")
    print("It's not a Perfect Number")
