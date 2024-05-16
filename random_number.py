import random
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)
random_number = generate_random_number(1, 99)
print(f"The random number is: {random_number}")
