######################################## IMPORTS AND INIT

import csv

######################################## GLOBAL VARIABLES

# Courses CSV file
CSV = "courses.csv"

######################################## MAIN

if __name__ == "__main__":
    # Print start message
    print("\nFETCHING DEPARTMENT LIST...")

    # Open and read from CSV file
    with open(CSV, newline="") as f:
        reader = csv.reader(f)
        # Add department to set
        mem = set()
        for row in reader:
            mem.add(row[3])
        # Print list of unique departments across all terms in alphabetical order
        depts = list(mem)
        depts.sort()
        print(depts)
    
    # Print completion message and quit
    print("PROCESS COMPLETE.")
    quit()


