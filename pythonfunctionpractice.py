# 1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

# Example usage:10

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = max_num(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {result}")

#2. Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
my_list = [2, 3, 4, 5]
result = mult_list(my_list)
print(f"The product of the numbers in the list is: {result}")

# 3. Write a Python function called rev_string() to reverse a string.
def rev_string(input_str):
    return input_str[::-1]

# Example usage:
original_str = "Hello, World!"
reversed_str = rev_string(original_str)
print(f"The reversed string is: {reversed_str}")

# 4. Write a Python function called num_within() to check whether a number falls in a given range.
#    The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#    Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False
def num_within(num, start, end):
    return num >= start and num <= end

# Example usage:
print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))


# 5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
   # The function accepts the number n, the number of rows to print
   # Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
    # Example:

def pascal(n):
    def generate_next_row(row):
        # Generate the next row of Pascal's triangle
        return [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    triangle = []
    for _ in range(n):
        current_row = generate_next_row(triangle[-1] if triangle else [1])
        triangle.append(current_row)

    # Print Pascal's triangle
    for row in triangle:
        print(row)

# Example usage:
n_rows = 5
pascal(n_rows)
