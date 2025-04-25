class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between a and b."""
        return a - b

    def divide(self, a, b):
        """Return the division of a by b. Raises an error if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage:
# calc = Calculator()
# print(calc.add(5, 3))        # Output: 8
# print(calc.subtract(5, 3))   # Output: 2
# print(calc.divide(6, 3))     # Output: 2.0
