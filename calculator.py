def perform_operations(x, y):
    print(f"Operations for {x} and {y}:")
    print("Addition:", x + y)
    print("Subtraction:", x - y)
    print("Multiplication:", x * y)
    if isinstance(x, int) and isinstance(y, int):
        if y != 0:
            print("Integer Division:", x // y)
        else:
            print("Integer Division: Division by zero error")
    else:
        print("Integer Division: Not applicable for floats")
    if y != 0:
        print("Floor Division:", x // y)
        print("Modulo Division:", x % y)
    else:
        print("Floor Division: Division by zero error")
        print("Modulo Division: Division by zero error")

a=int(input("Enter first number:"))
b=int(input("Enter second number"))
perform_operations(a, b)
