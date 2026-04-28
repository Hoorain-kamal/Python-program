# 4. Write a Python program to define a function that accepts two numbers and returns their GCD.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read inputs from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function and display result
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")