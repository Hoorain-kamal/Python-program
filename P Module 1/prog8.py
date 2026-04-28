# 3. Write a Python program to display the multiplication table of a given number.

num = int(input("Enter a number: "))

# Display multiplication table
print(f"\nMultiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")