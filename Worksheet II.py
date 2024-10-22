#seasion 3
#1 list 
course_name=["Introduction to Programming","calculus 1","Data Structures and Algorithms","Linear Algebra","Physics 1","Chemistry 1","BIology 1","Microeconomics","Macroeconomics","PSycology 1","History 1","English composition 1","Introduction to Philosophy","calculus 11","Discrete mathematics"]
print(course_name)

#lsit - sorted
sorted_course_name = sorted(course_name)
print(sorted_course_name)
sorted_course_name.reverse()
print(sorted_course_name)

#reverse
course_name.reverse()
print(course_name)
course_name.reverse()
print(course_name)

#sort()
course_name.sort()
print(course_name)
course_name.sort(reverse= True)
print(course_name)


course_name=["Linear Algebra","Physics 1","Chemistry 1","BIology 1","Microeconomics","Macroeconomics","PSycology 1","Introduction to Programming","calculus 1","Data Structures and Algorithms","History 1","English composition 1","Introduction to Philosophy","calculus 11","Discrete mathematics"]
print("The following courses are available for expression of interest if the students meet the prerequisites")
new_course=["Linear Algebra","Physics 1","Chemistry 1","BIology 1","Microeconomics","Macroeconomics","PSycology 1","Introduction to Programming","calculus 1","Data Structures and Algorithms","History 1","English composition 1","Introduction to Philosophy","calculus 11","business"]

print(f"new course :Discrete mathematics, orginal course : business")
#3
new_course.insert(0,"lab")
new_course.insert(8,"physical education")
new_course.append("chemistry")
print(new_course)
print(f"this course {course_name[0]},{course_name[8]},{course_name[11]} and {[12]}are unavailable due to technical and room availability issues")
new_course.pop(0)
new_course.pop(8)
new_course.pop(11)
print(f"the avalable courses are {new_course}and the no longer available courses are ")
# list of tuples
#Tuleps and loops

# Createing a list of tuples (course_id, course_name)
courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
]

# 1.2: Createing an empty list to store course names
course_names = []

# : Looping through each tuple in the list
for course in courses:
    #  2.1: Extracting the course ID and name from the tuple
    course_id, course_name = course  

    #  2.2: Adding the course name to the empty list
    course_names.append(course_name)

print("The following courses are available:")
for name in course_names:
    print(name)  
#session 4 
departments_info = [
    (1, "Business"),
    (2, "news and media"),
    (3, "history"),
    (4, "life lessions"),
    (5, "theeoritical physics"),
    (6, "life of pie"),
    (7, "penetration testing"),
    (8, "linux"),
    (9, "pycharm"),
    (10, "javascript"),
    (11, "java"),
    (12, "HTMl"),
    (13, "Magneto"),
    (14, "computer fundemental"),
    (15, "ict data analytics")
]

while True:
    course_id = input("Enter a course ID (1-15) or type 'quit' or '0' to exit: ") 
    if  course_id == '0' or course_id == "quit":  
        print("Exiting the program.")  
        break  

    if course_id.isdigit():  
        int_course_id = int(course_id)  
        
        if 1 <= int_course_id <= 15:  
            find = False 
            for department in departments_info:
                if department[0] == int_course_id:  
                    print(f"Course ID {int_course_id} is in the {department[1]} department.")  
                    find = True  
                    break  
            
            if not find:  
                print("Course ID not found.") 
        else:
            print("Course ID is out of range , try again in between 1-15.") 
    else:
        print("Please enter a valid number or 'quit' to exit.")