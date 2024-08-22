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

# Input marks for each subject manually
subjects = ["English", "Math", "Nepali", "Social Studies", "Science"]
marks = {}

print("Enter marks out of 100 for the following subjects:")
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

# Calculate the percentage
percentage = calculate_percentage(marks)

# Determine the division
division = determine_division(percentage)

# Print the results
print(f"\nPercentage obtained: {percentage:.2f}%")
print(f"Division: {division}")
