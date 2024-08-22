# Function to calculate the percentage
def calculate_percentage(marks):
    total_marks = sum(marks.values())
    total_subjects = len(marks)
    percentage = (total_marks / (total_subjects * 100)) * 100
    return percentage

# Function to determine the division based on percentage
def determine_division(percentage):
    if percentage >= 80:
        return "Distinction"
    elif percentage >= 60:
        return "First Division"
    elif percentage >= 45:
        return "Second Division"
    elif percentage >= 32:
        return "Third Division"
    else:
        return "Fail"

# Function to input and store marks for multiple students
def input_student_marks():
    students = {}
    while True:
        name = input("\nEnter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        marks = {}
        print(f"Enter marks out of 100 for {name}:")
        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"{subject}: "))
                    if 0 <= mark <= 100:
                        marks[subject] = mark
                        break
                    else:
                        print("Please enter a valid mark between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
        
        students[name] = marks
    return students

# Function to calculate and display the results for all students
def display_results(students):
    print("\nStudent Results:")
    for name, marks in students.items():
        percentage = calculate_percentage(marks)
        division = determine_division(percentage)
        print(f"\n{name}:")
        print(f"  Percentage: {percentage:.2f}%")
        print(f"  Division: {division}")

# Define the subjects
subjects = ["English", "Math", "Nepali", "Social Studies", "Science"]

# Input marks for multiple students
students = input_student_marks()

# Display the results
display_results(students)
