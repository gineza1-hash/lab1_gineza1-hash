# Grade Evaluator & Archiver

## Files
- grade-evaluator.py : Python script to calculate GPA and student status
- organizer.sh : Bash script to archive grades.csv
- grades.csv : Input data

## How to Run

### Run the Python program
python3 grade-evaluator.py

Enter the filename when prompted.

### Run the Shell Script
chmod +x organizer.sh
./organizer.sh

This will:
- Move grades.csv into the archive folder
- Add a timestamp to the file
- Create a new empty grades.csv
- Log the action in organizer.log