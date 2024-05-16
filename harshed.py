def is_harshad_number(number):
    sum_of_digits = sum(int(digit) for digit in str(number))
    return number % sum_of_digits == 0

number = int(input("Enter number: "))
if is_harshad_number(number):
    print("Given number is Harshad number")
else:
    print("Given number is not Harshad number")
