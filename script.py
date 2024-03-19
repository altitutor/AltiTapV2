import os
import re
from tkinter import Tk, Label, OptionMenu, StringVar

# Paths to the directories
students_folder_path = 'students'
classes_folder_path = 'classes'

# Function to extract class file paths from a student Markdown file
def extract_class_paths(file_content):
    # Extracting both types of references
    class_references = re.findall(r'\[\[(1\.2 Classes/)?(.*?)\|', file_content)

    standardized_paths = []
    for _, path in class_references:
        # Ensure the path ends with .md
        if not path.endswith('.md'):
            path += '.md'
        standardized_paths.append(path)

    return standardized_paths


def update_students_dropdown(*args):
    selected_day = day_var.get()
    students = load_students_by_day(selected_day)
    students_var.set('Select a student')  # Reset the student dropdown
    student_dropdown['menu'].delete(0, 'end')  # Clear existing options
    for student in students:
        student_dropdown['menu'].add_command(label=student, command=lambda value=student: students_var.set(value))

# Function to read class details from a class Markdown file
def read_class_details(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            details = re.search(r'---\s+Day: (.+?)\s+Subject: (.+?)\s+Time: (.+?)\s+---', content, re.DOTALL)
            if details:
                return details.groups()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return None

def load_students_by_day(selected_day):
    students_by_day = []
    for student_file in os.listdir(students_folder_path):
        if student_file.endswith('.md'):
            with open(os.path.join(students_folder_path, student_file), 'r', encoding='utf-8') as file:
                content = file.read()
                class_paths = extract_class_paths(content)
                for class_path in class_paths:
                    # Assuming all class files are directly under 'classes' folder
                    class_file_path = os.path.join(classes_folder_path, class_path)
                    class_details = read_class_details(class_file_path)
                    if class_details and class_details[0] == selected_day:
                        students_by_day.append(student_file[:-3])  # Remove .md extension
                        break
    return students_by_day


# Initialize Tkinter window
root = Tk()
root.title('Class Schedule Viewer')

# Dropdown for selecting a day
day_var = StringVar(root)
day_var.set("Select a day")
days = ["1.Monday", "2.Tuesday", "3.Wednesday", "4.Thursday", "6.Saturday AM", "6.Saturday PM", "7.Sunday AM", "7.Sunday PM"]
day_dropdown = OptionMenu(root, day_var, *days)
day_dropdown.pack()

# Function to update students dropdown based on selected day
def update_students_dropdown(*args):
    selected_day = day_var.get()
    students = load_students_by_day(selected_day)
    students_var.set('Select a student')
    student_dropdown['menu'].delete(0, 'end')
    for student in students:
        student_dropdown['menu'].add_command(label=student, command=lambda value=student: students_var.set(value))

# Dropdown for selecting a student
students_var = StringVar(root)
students_var.set("Select a student")
student_dropdown = OptionMenu(root, students_var, "Select a day first")
student_dropdown.pack()

# Link the day selection with student dropdown update
day_var.trace('w', update_students_dropdown)

root.mainloop()
