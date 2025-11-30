"""
json_practice.py

Program to practice loading, modifying, and dumping JSON data.

Requirements:
1. Use json.load() to load student.json into a Python list.
2. Define a function to loop through and print student details.
3. Print original list, append new student data, print updated list.
4. Use json.dump() to write the updated list back to student.json.
"""

import json
import sys
import os

FILENAME = 'student.json'

def print_student_list(student_list, title):
    """
    Loops through the student list and prints each student's details.
    """
    print(f"\n--- {title} ---")
    if not student_list:
        print("The student list is empty.")
        return

    for student in student_list:
        f_name = student.get("F_Name", "N/A")
        l_name = student.get("L_Name", "N/A")
        student_id = student.get("Student_ID", "N/A")
        email = student.get("Email", "N/A")

        print(f"{l_name}, {f_name} : ID = {student_id} , Email = {email}")

def main():
    # --- 1. Load the JSON file into a Python list ---
    if not os.path.exists(FILENAME):
        print(f"Error: {FILENAME} not found. Please ensure the file is in the same directory.")
        sys.exit(1)

    try:
        with open(FILENAME, 'r') as f:
            student_data = json.load(f)

        # Ensure data loaded is a list
        if not isinstance(student_data, list):
            print(f"Error: {FILENAME} content is not a list. Exiting.")
            sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {FILENAME}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        sys.exit(1)

    # --- 2. Print Original List ---
    print_student_list(student_data, "Original Student List")

    # --- 3. Add new data using append() ---

    # NOTE: CHANGE THE PLACEHOLDER VALUES BELOW TO YOUR FICTIONAL DATA
    new_student = {
        "F_Name": "[Your First Name]",  # Replace with your First Name
        "L_Name": "[Your Last Name]",    # Replace with your Last Name
        "Student_ID": 99999,             # Replace with your fictional ID
        "Email": "myemail@example.com"   # Replace with your fictional email
    }

    student_data.append(new_student)

    # --- 4. Print Updated List ---
    print_student_list(student_data, "Updated Student List")

    # --- 5. Use JSON dump() to append (overwrite with new content) ---
    try:
        # Using 'w' mode overwrites the existing file with the updated list.
        with open(FILENAME, 'w') as f:
            # The indent=4 makes the JSON file human-readable
            json.dump(student_data, f, indent=4)

        # --- 6. Output Notification ---
        print(f"\nNotification: The {FILENAME} file was successfully updated with the new data.")

    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")

if __name__ == '__main__':
    main()