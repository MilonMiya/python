# 1. A List of student names
# We use a List here because student names might be added or removed later.
students_list = ["Milon", "Rakib", "Sajid", "Anika"]

# 2. A Tuple for fixed information
# Department info usually stays constant, so a Tuple is ideal for security and speed.
department_info = ("Computer Science", "CSE-101", "Dhaka, Bangladesh")

print("--- Initial Data ---")
print(f"Department: {department_info[0]}")
print(f"Current Students: {students_list}")

# --- List Operations ---

# Adding a new student to the list
students_list.append("Tanvir") 

# Removing a student from the list
students_list.remove("Rakib")

# Sorting the list in alphabetical order
students_list.sort()

print("\n--- After Modification (List) ---")
print(f"Updated Student List: {students_list}")
print(f"Total Students: {len(students_list)}")


# --- Tuple Operations ---

# Tuple Unpacking: Assigning tuple values to individual variables
dept_name, course_code, location = department_info

print("\n--- Tuple Details ---")
print(f"Course: {course_code}")
print(f"Location: {location}")


# --- Loop and Conditional Usage ---

print("\n--- Student Verification ---")
search_name = "Milon"

# Checking if a specific name exists in the list
if search_name in students_list:
    print(f"Yes, {search_name} is in the {dept_name} list.")
else:
    print(f"No, {search_name} is not found.")

# Slicing: Getting the first two students from the list
top_two = students_list[:2]
print(f"First two students: {top_two}")