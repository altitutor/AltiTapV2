import os
import re
import json
from datetime import datetime

# Updated Paths to the directories
students_folder_path = '/Users/altitutoreducation/Library/Mobile Documents/iCloud~md~obsidian/Documents/Altitutor Admin/1.1 Students'
classes_folder_path = '/Users/altitutoreducation/Library/Mobile Documents/iCloud~md~obsidian/Documents/Altitutor Admin/1.2 Classes'
google_drive_path = '/Users/altitutoreducation/Library/CloudStorage/GoogleDrive-admin@altitutor.com/My Drive'

# Function to extract class file paths from a student Markdown file
def extract_class_paths(file_content):
    class_references = re.findall(r'\[\[(1\.2 Classes/)?(.*?)\|', file_content)
    standardized_paths = []
    for _, path in class_references:
        if not path.endswith('.md'):
            path += '.md'
        standardized_paths.append(path)
    return standardized_paths

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
                    class_file_path = os.path.join(classes_folder_path, class_path)
                    class_details = read_class_details(class_file_path)
                    if class_details and class_details[0] == selected_day:
                        students_by_day.append(student_file[:-3])  # Remove .md extension
                        break
    return students_by_day

def get_current_day_with_ampm():
    current_weekday = datetime.now().weekday()
    current_time = datetime.now().time()

    if current_weekday == 5 and (current_time.hour > 12 or (current_time.hour == 12 and current_time.minute > 30)):
        return "6.Saturday PM"
    elif current_weekday == 6 and (current_time.hour > 12 or (current_time.hour == 12 and current_time.minute > 30)):
        return "7.Sunday PM"
    else:
        weekday_to_day = {
            0: "1.Monday",
            1: "2.Tuesday",
            2: "3.Wednesday",
            3: "4.Thursday",
            4: "5.Friday", # If Friday is not used, you can remove or adjust this
            5: "6.Saturday AM",
            6: "7.Sunday AM",
        }
        return weekday_to_day.get(current_weekday)

selected_day_str = get_current_day_with_ampm()
if selected_day_str:
    students_list = load_students_by_day(selected_day_str)

    # Define the JSON content
    json_content = json.dumps({'names': students_list}, indent=4)

    # Save to the root directory
    with open('names.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_content)
    
    # Save to the specified Google Drive path
    google_drive_file_path = os.path.join(google_drive_path, 'names.json')
    with open(google_drive_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_content)

    print(f"Names for {selected_day_str} written to names.json in both locations.")
else:
    print("Today is not a day for classes according to the provided mapping.")
