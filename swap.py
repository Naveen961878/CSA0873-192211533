def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x = 5
y = 10
print(f"Original values: x = {x}, y = {y}")
x, y = swap_with_temp(x, y)
print(f"Swapped values: x = {x}, y = {y}")
