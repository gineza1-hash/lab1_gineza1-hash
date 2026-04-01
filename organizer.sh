#!/usr/bin/env bash

# Create archive directory if it does not exist
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Generate timestamp
timestamp=$(date +"%Y%m%d-%H%M%S")

# Rename file
new_name="grades_$timestamp.csv"

# Move the file
mv grades.csv archive/$new_name

# Create new empty grades.csv
touch grades.csv

# Logging
echo "$timestamp | grades.csv -> archive/$new_name" >> organizer.log

echo "Archiving complete."