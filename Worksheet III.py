#Week 5
#1)student coursee enrollment 
# creating a dictiornary 
enrollments = [
    (1001, 'CS101', 'S1'),
    (1001, 'MATH101', 'S1'),
    (1002, 'CS101', 'S1'),
    (1002, 'MATH102', 'S2'),
    (1003, 'CS202', 'S2'),
    (1003, 'PHY101', 'S1'),
    (1004, 'CS202', 'S2'),
    (1004, 'CHEM101', 'S1'),
    (1005, 'BIO101', 'S1'),
    (1005, 'HIST101', 'S1'),
    (1006, 'BIO102', 'S2'),
    (1006, 'ENGL101', 'S1'),
    (1007, 'ECON101', 'S1'),
    (1007, 'PSY101', 'S1'),
    (1008, 'ECON102', 'S2'),
    (1008, 'SOC101', 'S1'),
    (1009, 'PSY102', 'S2'),
    (1009, 'SOC102', 'S2'),
    (1010, 'CS101', 'S1'),
    (1010, 'MATH101', 'S1')
]
course_enrollments = {}

# Loop through the dictionary to print out each students name and their enrolled courses
for student_id, course_code, _ in enrollments:
    if student_id not in course_enrollments:
        course_enrollments[student_id] = []  
    course_enrollments[student_id].append(course_code)
for student_id, courses in course_enrollments.items():
    print(f"Student ID: {student_id} = Enrolled Courses: {': '.join(courses)}")
#2)class schedule
courses = [
    ('CS101', 'Introduction to Computer Science', 'Computer Science', 'S1'),
    ('CS202', 'Data Structures and Algorithms', 'Computer Science', 'S2'),
    ('MATH101', 'Calculus I', 'Mathematics', 'S1'),
    ('MATH102', 'Calculus II', 'Mathematics', 'S2'),
    ('PHY101', 'General Physics I', 'Physics', 'S1'),
    ('PHY102', 'General Physics II', 'Physics', 'S2'),
    ('CHEM101', 'General Chemistry I', 'Chemistry', 'S1'),
    ('CHEM102', 'General Chemistry II', 'Chemistry', 'S2'),
    ('BIO101', 'Biology I', 'Biology', 'S1'),
    ('BIO102', 'Biology II', 'Biology', 'S2'),
    ('HIST101', 'American History I', 'History', 'S1'),
    ('HIST102', 'American History II', 'History', 'S2'),
    ('ENGL101', 'English Composition I', 'English', 'S1'),
    ('ENGL102', 'English Composition II', 'English', 'S2'),
    ('ECON101', 'Principles of Economics', 'Economics', 'S1'),
    ('ECON102', 'Intermediate Microeconomics', 'Economics', 'S2'),
    ('PSY101', 'Introduction to Psychology', 'Psychology', 'S1'),
    ('PSY102', 'Developmental Psychology', 'Psychology', 'S2'),
    ('SOC101', 'Introduction to Sociology', 'Sociology', 'S1'),
    ('SOC102', 'Social Problems', 'Sociology', 'S2')
]
departments = {}
for course_id, course_name, department, semester in courses:
    if department not in departments:
        departments[department] = [] 
    departments[department].append((department, course_id, course_name))  

for department, course_list in departments.items():
    for _, course_id, course_name in course_list:
        print(f"Course Name: {course_name}, Department: {department}")
#3)lecture asighnment 
lecturer_courses = {
    "Dr. John Doe": ["Introduction to Computer Science"],
    "Mr. Michael Johnson": ["General Physics II"],
    "Asst. Prof. Olivia Taylor": ["General Chemistry I"],
    "Dr. Emily Brown": ["Calculus II"],
    "Prof. David Lee": ["General Physics I"],
    "Miss. Sophia Carter": ["Biology I", "Biology II"],
    "Dr. Oliver Hernandez": ["English Composition I"],
    "Prof. Isabella Garcia": ["Introduction to Sociology"],
    "Prof. Evelyn Russell": ["Principles of Economics", "Intermediate Microeconomics"],
    "Dr. Lucas Sanchez": ["Introduction to Psychology", "Developmental Psychology"],
    "Asst. Prof. Liam Lopez": ["Social Problems"]
}

# Loop through the dictionary and print the teachers name and the course they teach
for lecturer, courses in lecturer_courses.items():
    print(f"Lectur name: {lecturer}, Course name: {', '.join(courses)}")
 
 #session 6
class_list = []

while True:
    student_name = input("Enter the student's name (or type 'exit' to finish): ")
    if student_name.lower() == 'exit':
        break
    class_list.append(student_name)
    print(f"You have added {student_name} to your class.")

# Print the final class list
print("\nFinal class list:")
for student in class_list:
    print(student)
# Room data
rooms = [
    {"RoomNumber": 101, "Capacity": 15, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 102, "Capacity": 15, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 103, "Capacity": 20, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 104, "Capacity": 20, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 105, "Capacity": 25, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 106, "Capacity": 25, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 107, "Capacity": 30, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 108, "Capacity": 30, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 109, "Capacity": 30, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 110, "Capacity": 10, "FloorNumber": "Ground Floor", "Location": "Building A"},
    {"RoomNumber": 201, "Capacity": 10, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 202, "Capacity": 10, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 203, "Capacity": 25, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 204, "Capacity": 25, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 205, "Capacity": 30, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 206, "Capacity": 40, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 207, "Capacity": 40, "FloorNumber": "1st Floor", "Location": "Building A"},
    {"RoomNumber": 208, "Capacity": 40, "FloorNumber": "1st Floor", "Location": "Building A"},
]

# Class list management
class_list = []
max_students = 10
active = True

while active:
    student_name = input("Enter the student's name (or type 'exit', 'quit', or '0' to finish): ")
    
    if student_name.lower() in ['exit', 'quit', '0']:
        active = False
        print(f"\nTotal number of students entered: {len(class_list)}")
        print("Students:")
        for student in class_list:
            print(student)
        continue  

    if len(class_list) >= max_students:
        print(f"Maximum number of students ({max_students}) reached. Exiting...")
        break

    class_list.append(student_name)
    print(f"You have added {student_name} to your class.")

# Room capacity check
while True:
    try:
        min_capacity = int(input("Enter the minimum number of seats required for the class (or type '0' to exit): "))
        if min_capacity == 0:
            break
        
        suitable_rooms = [room for room in rooms if room["Capacity"] >= min_capacity]
        
        if suitable_rooms:
            for room in suitable_rooms:
                print(f"Room {room['RoomNumber']} with capacity {room['Capacity']} is available on {room['FloorNumber']}, {room['Location']}.")
        else:
            print("No suitable rooms found for the requested capacity.")
    
    except ValueError:
        print("Please enter a valid number.")

# Infinite loop for additional input
print("\nPress CTRL-C to stop entering inputs.")
line_count = 0

try:
    while True:
        u_input = input("Enter a line of text: ")
        print(u_input)
        line_count += 1
except KeyboardInterrupt:
    print(f"\nNo of lines entered : {line_count}")