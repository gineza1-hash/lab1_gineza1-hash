import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    # Variables to track totals
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    formative_score = 0
    summative_score = 0

    failed_formative = []

    # Validate scores and calculate totals
    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']
        assignment = item['assignment']

        # Score validation
        if score < 0 or score > 100:
            print(f"Invalid score for {assignment}")
            return

        total_weight += weight

        if group == "Formative":
            formative_weight += weight
            formative_score += (score * weight) / 100

            if score < 50:
                failed_formative.append(item)

        elif group == "Summative":
            summative_weight += weight
            summative_score += (score * weight) / 100

    # Weight validation
    if total_weight != 100:
        print("Error: Total weights must equal 100.")
        return

    if formative_weight != 60:
        print("Error: Formative weights must equal 60.")
        return

    if summative_weight != 40:
        print("Error: Summative weights must equal 40.")
        return

    # Calculate total grade
    total_grade = formative_score + summative_score

    # GPA calculation
    gpa = (total_grade / 100) * 5.0

    print(f"Total Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")

    # Pass/Fail decision
    formative_percentage = (formative_score / formative_weight) * 100
    summative_percentage = (summative_score / summative_weight) * 100

    if formative_percentage >= 50 and summative_percentage >= 50:
        print("Final Status: PASSED")
    else:
        print("Final Status: FAILED")

        # Resubmission logic
        if failed_formative:
            highest_weight = max(item['weight'] for item in failed_formative)

            print("\nAssignments eligible for resubmission:")
            for item in failed_formative:
                if item['weight'] == highest_weight:
                    print(f"- {item['assignment']}")
if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)                 