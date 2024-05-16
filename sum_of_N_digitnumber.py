
N = int(input("Enter N value: "))
number = input(f"Enter {N} digit number: ")
while len(number) > 1:
    total = 0
    for digit in number:
        total += int(digit)  
    number = str(total)
print(f"Sum of {N} digit number: {number}")
