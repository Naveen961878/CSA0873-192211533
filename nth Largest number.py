def find_nth_largest_number(numbers, n):
    if not numbers or n < 1 or n > len(numbers):
        return None 
    unique_numbers = sorted(set(numbers), reverse=True)  
    if n <= len(unique_numbers):
        return unique_numbers[n - 1]
    else:
        return None  
numbers = [14,67,48,23,5,62]
n = 4
nth_largest_number = find_nth_largest_number(numbers, n)
if nth_largest_number is not None:
    print(f"The {n}th largest number is:", nth_largest_number)
else:
    print(f"There are not enough unique numbers in the list to find the {n}th largest number.")
