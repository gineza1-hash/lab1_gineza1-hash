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