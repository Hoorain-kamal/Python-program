import os.path
import sys

fname = input("Enter the filename to sort: ")

# Check if file exists
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

# Read file
infile = open(fname, "r")
lines = infile.readlines()
infile.close()

# Remove newline characters
linelist = []
for line in lines:
    linelist.append(line.strip())

# Sort lines
linelist.sort()

# Write to new file
outfile = open("sorted.txt", "w")

for line in linelist:
    outfile.write(line + "\n")

outfile.close()

# Display result
print("sorted.txt created with", len(linelist), "sorted lines")

# Optional: read and print content
outfile = open("sorted.txt", "r")
print("Content of sorted.txt:")
print(outfile.read())
outfile.close()