def improved_function_with_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
result = improved_function_with_error_handling(5, 0)
print(f"Result: {result}")

result = improved_function_with_error_handling("5", 2)
print(f"Result: {result}")

result = improved_function_with_error_handling(5, 2)
print(f"Result: {result}")

result = improved_function_with_error_handling(5, "a")
print(f"Result: {result}") # Demonstrates improved error handling 