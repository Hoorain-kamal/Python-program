name = input("Enter student name: ")
dob = input("Enter date of birth: ")
reg_no = input("Enter register number: ")
dept = input("Enter department: ")

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total/5

print("\n--- STUDENT DETAILS ---")
print("Name:", name)
print("DOB:", dob)
print("Register Number:", reg_no)
print("Department:", dept)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 85:
    print("Result: Distinction")
elif percentage >=65:
    print("Result:1st class ")
elif percentage >=50:
    print("Result: second class")
elif percentage >=35:
    print("Result : Third class")
else: 
    print("Result : Fail")
