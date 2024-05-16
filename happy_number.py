def is_happy_number(number):
    def get_next_number(n):
        return sum(int(digit)**2 for digit in str(n))
    
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = get_next_number(number)
    return number == 1

number = int(input("Enter number: "))
if is_happy_number(number):
    print("Given number is happy number")
else:
    print("Given number is not happy number")
