######################################## IMPORTS AND INIT

import os
import csv
import pymongo
from dotenv import load_dotenv
load_dotenv()

######################################## GLOBAL VARIABLES

# MongoDB connection
DB_URI = os.getenv("DB_URI")
CLIENT = pymongo.MongoClient(DB_URI)

# Courses CSV file
CSV = "courses.csv"

######################################## MAIN

if __name__ == "__main__":
    # Print start message
    print("\nINSERTING INTO DATABASE...")

    # Get database and courses collection
    database = CLIENT.Cluster0
    collection = database.courses

    # Open and read from CSV file
    with open(CSV, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            course = {
                "courseSummary": {
                    "catalog": row[0],
                    "title": row[1],
                    "instructor": row[2],
                    "department": row[3],
                    "term": row[4],
                    "url": row[5],
                },
                "courseStat": {
                    "enrollment": float(row[6]),
                    "responses": float(row[7]),
                    "ratio": float(row[8]),
                },
                "courseRating": {
                    "overall": float(row[9]),
                    "materials": float(row[10]),
                    "assignments": float(row[11]),
                    "feedback": float(row[12]),
                    "section": float(row[13]),
                },
                "instructorRating": {
                    "overall": float(row[14]),
                    "lectures": float(row[15]),
                    "accessibility": float(row[16]),
                    "enthusiasm": float(row[17]),
                    "encouragement": float(row[18]),
                    "feedback": float(row[19]),
                    "returning": float(row[20]),
                },
                "courseEval": {
                    "workload": float(row[21]),
                    "recommend": float(row[22]),
                    "sentiment": float(row[23]),
                },
            }
            collection.insert_one(course)
    
    # Print completion message and quit
    print("PROCESS COMPLETE.")
    quit()


