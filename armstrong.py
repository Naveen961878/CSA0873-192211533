def is_armstrong(number):
    num_digits = len(str(number))
    total = sum(int(digit)**num_digits for digit in str(number))
    return total == number
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


