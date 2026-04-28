#4. Using lambda – Sorting by Second Element of Tuples
# Program to sort a list of tuples based on the second element

data = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted Data:", sorted_data)
