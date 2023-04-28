def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Prompt user to input a number
num = int(input("Enter a number: "))

# Call the function to check whether the number is even or odd
result = check_even_odd(num)

# Print the result to the user
print(f"The number {num} is {result}.")
