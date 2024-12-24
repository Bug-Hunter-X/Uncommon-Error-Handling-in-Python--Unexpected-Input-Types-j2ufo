def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example usage where the bug will occur
result = function_with_uncommon_error(5, 0)
print(f"Result: {result}")

result = function_with_uncommon_error("5", 2)
print(f"Result: {result}")

result = function_with_uncommon_error(5, 2)
print(f"Result: {result}")