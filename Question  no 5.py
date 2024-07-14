
import numpy as np

# Get filename from user for extracting the data
filename = input("Enter the filename: ")

# Read the input file
with open(filename, 'r') as f:
    # Read the first line (number of students and coursework weight)
    line = f.readline().strip().split()
    num_students = int(line[0])
    coursework_weight = float(line[1])
    
    # Initialize a NumPy array to store student marks
    marks_array = np.array([[0, 0.0, 0.0, 0.0]] * num_students)
    
    # Read remaining lines (student marks-registration number , exam marks , and coursework marks)
    for i in range(num_students):
        line = f.readline().strip().split()
        reg_num = int(line[0])
        exam_mark = float(line[1])
        coursework_mark = float(line[2])
        
        # Calculate the overall mark with the formula
        overall_mark = round((1 - coursework_weight/100) * exam_mark + (coursework_weight/100) * coursework_mark)
        marks_array[i] = [reg_num, exam_mark, coursework_mark, overall_mark]

# establish structure data type for establishing student information
students_dtype = np.dtype([('reg_num', 'i4'), ('exam_mark', 'f8'), ('coursework_mark', 'f8'), ('overall_mark', 'i4'), ('grade', 'U10')])

# Initialize a second NumPy array
students_array = np.zeros(num_students, dtype=students_dtype)

# Assign values to the second array and hence calculate the grade
for i in range(num_students):
    reg_num = marks_array[i][0]
    exam_mark = marks_array[i][1]
    coursework_mark = marks_array[i][2]
    overall_mark = marks_array[i][3]
    
    # Determine the grade according to the criteria mentioned
    if exam_mark < 30 or coursework_mark < 30:
        grade = 'Fail'
    elif overall_mark >= 70:
        grade = '1st'
    elif overall_mark >= 50:
        grade = '2nd'
    elif overall_mark >= 40:
        grade = '3rd'
    else:
        grade = 'Fail'
        
    students_array[i] = (reg_num, exam_mark, coursework_mark, overall_mark, grade)

# Sort the second array based on the overall marks of the student
students_array.sort(order='overall_mark')

# Output the second array to a file
with open('output.txt', 'w') as f:
    print(students_array, file=f)

# Display the count of students in each grade category and provide the registration numbers of those who did not pass.
num_first = np.count_nonzero(students_array['grade'] == '1st')
num_second = np.count_nonzero(students_array['grade'] == '2nd')
num_third = np.count_nonzero(students_array['grade'] == '3rd')
num_fail = np.count_nonzero(students_array['grade'] == 'Fail')

print("Number of first-class students: {}".format(num_first))
print("Number of second-class students: {}".format(num_second))
print("Number of third-class students: {}".format(num_third))
print("Number of failed students: {}".format(num_fail))

# Extract registration numbers of students who failed and print the list of failed students' registration numbers.
failed_students = students_array['reg_num'][students_array['grade'] == 'Fail']
print("Registration numbers of failed students: {}".format(failed_students))
