import sys

def load_students(file):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    with open(file) as file:
        lines = file.readlines()
        # TODO: Split each line by comma
        students = []
        for line in lines[1:]:
            name, age, grade, subject = line.strip().split(",") 
            students.append(
                {
                    'name': name,
                    'age': int(age),
                    'grade': int(grade),
                    'subject': subject
                }
            )
            # TODO: Return list of student data
        return students
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    total = 0
    for student in students:
        total += student['grade']
    # TODO: Sum all grades
    average = total/len(students)
    # TODO: Divide by number of students
    return average
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    math_count = 0
    for student in students:
        if student['subject'] == "math":
            math_count += 1
    return math_count
    pass

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    report = f"Average grade: {average:.1f} Math Student Count: {math_count} Student Count: {total}"
    return report 
    pass

def save_report(report, file):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    with open('output/analysis_results.txt', 'w') as file:
        file.write(f"{report}\n")
    pass

def main():
    file = sys.argv[1]
    # TODO: Load data
    student_info = load_students(file)
    # TODO: Calculate statistics
    ave = calculate_average_grade(student_info)
    print(f'{ave}')
    math = count_math_students(student_info)
    print(f'{math}')
    # TODO: Generate and save report
    save_report(generate_report(len(student_info),ave,math), student_info)
    pass

if __name__ == "__main__":
    main()
