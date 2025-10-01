import sys

def load_data(file):
    """Load data from CSV file."""
    # TODO: Check file extension
    if file.endswith(".csv"):
        print("Correct File")
    # TODO: Call appropriate loader
    pass

def load_csv(file):
    """Load CSV data."""
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
    # TODO: Same technique as basic script
    pass

def analyze_data(students):
    """Analyze student data."""
    # TODO: Calculate multiple statistics
    # TODO: Return dictionary of results
    max_grade = 0
    min_grade = 100
    subjects = {"English": 0, "PE": 0, "History": 0, "Chemistry": 0, "Art": 0, "Biology": 0 }
    for student in students:
        if student['grade'] >= max_grade:
            max_grade = student['grade']
        if student['grade'] <= min_grade:
            min_grade = student['grade']
            
        if student['subject'] == "English":
            subjects["English"] += 1
        if student['subject'] == "PE":
            subjects["PE"] += 1
        if student['subject'] == "History":
            subjects["History"] += 1
        if student['subject'] == "Chemistry":
            subjects["Chemistry"] += 1
        if student['subject'] == "Art":
            subjects["Art"] += 1
        if student['subject'] == "Biology":
            subjects["Biology"] += 1
    return max_grade, min_grade, subjects 
    pass

def analyze_grade_distribution(students):
    """Count grades by letter grade."""
    # TODO: Count A (90-100), B (80-89), etc.
    letter_grades = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
        }
    for student in students:
        if student['grade'] >= 90:
            letter_grades['A (90-100)'] += 1
        if student['grade'] >= 80:
            letter_grades['B (80-89)'] += 1
        if student['grade'] >= 70:
            letter_grades['C (70-79)'] += 1
        if student['grade'] >= 60:
            letter_grades['D (60-69)'] += 1
        else:
            letter_grades['F (0-59)'] += 1
    return letter_grades
    pass

def save_results(letter_grades, max_grade, min_grade, subjects):
    """Save detailed results."""
    # TODO: Format and write comprehensive report
    with open('output/analysis_results.txt', 'a') as file:
        file.write(f'Grade Distrobustion: {letter_grades}\n')
        file.write(f'Maximum Grade: {max_grade}\n')
        file.write(f'Minimum Grade: {min_grade}\n')
        file.write(f'Student Subjects: {subjects}\n')
    pass

def main():
    # TODO: Orchestrate the analysis
    file = load_csv(sys.argv[1])

    print(analyze_data(file))
    max_grade, min_grade, subjects = analyze_data(file)
    print(analyze_grade_distribution(file))
    save_results(analyze_grade_distribution(file), max_grade, min_grade, subjects)
    pass

if __name__ == "__main__":
    main()