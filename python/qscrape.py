######################################## IMPORTS AND INIT

import os
import time
import math
import csv
import flair
import traceback
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
load_dotenv()

######################################## GLOBAL VARIABLES

# Harvard Key authentication parameters
ORIGIN = "https://www.pin1.harvard.edu"
LOGIN_PATH = "/cas/login?service=https%3A%2F%2Fkey.harvard.edu%2Fmanage-account"
USER_LOGIN = os.getenv("USER_LOGIN")        # Insert Harvard Email
USER_PASSWORD = os.getenv("USER_PASSWORD")  # Insert password

# QGuide URLs
OLD_URL = "https://course-evaluation-reports.fas.harvard.edu/fas/list?"
NEW_URL = "https://qreports.fas.harvard.edu/browse/index?"

# Chrome webdriver
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument('log-level=3')
CHROME = webdriver.Chrome(service=Service(executable_path=r'/usr/local/bin/chromedriver'), options=OPTIONS)

# Courses CSV file
CSV = "spring2023.csv" # "courses.csv"

# Sentiment analysis model
FLAIR = flair.models.TextClassifier.load('en-sentiment')

######################################## FUNCTIONS

# Custom string to float conversion (non-float strings become -1.0)
def string_to_float(s):
    # Begin try-exception branch
    try:
        return float(s)
    except:
        return float("nan")

# Harvard Key authentication
def auth():
    # Print starting message
    print("\nLOGGING INTO HARVARD KEY...")

    # Begin try-exception branch
    try:
        # Navigate to login page and delay for rendering purposes
        url = ORIGIN + LOGIN_PATH
        CHROME.get(url)
        time.sleep(0.5)

        # Input credentials and await 2FA
        CHROME.find_element("name", "username").send_keys(USER_LOGIN)
        CHROME.find_element("name", "password").send_keys(USER_PASSWORD)
        input("AWAITING 2FA (PRESS ENTER WHEN FINISHED)...")

        # Return success
        print("LOGIN SUCCESS.\n")
        return 0
    except Exception as e:
        # Return failure
        print("LOGIN FAILED: " + str(e) + ".\n")
        return 1

# Scrape the old QGuide
def qscrape_old():
    # Print starting message
    print("SCRAPING OLD QGUIDE DATA...")

    # Begin try-exception branch
    try:
        # Navigate to old QGuide page
        CHROME.get(OLD_URL)
        
        '''
        IMPLEMENTATION NEEDED
        '''

        # Return success
        print("SCRAPE SUCCESS.\n")
        return 0
    except Exception as e:
        # Return failure
        print("SCRAPE FAILED: " + str(e) + ".\n")
        return 1

# Scrape the new QGuide
def qscrape_new():
    # Define some helper functions for scraping
    def get_course_responses(source):
        # Gather response info
        responses = source
        course_enrolled = string_to_float(responses.find("td", attrs={"headers": "hdGroup0 InvitedCount"}).string)
        course_evals = string_to_float(responses.find("td", attrs={"headers": "hdGroup0 RespCount"}).string)
        course_ratio = string_to_float(str(math.floor((course_evals / course_enrolled) * 100)))
        return [course_enrolled, course_evals, course_ratio]

    def get_course_ratings(source):
        # Gather course rating means
        ratings = source
        table = ratings.find_all("tr", attrs={"class": "CondensedTabularOddRows"})
        table = [i.contents for i in table]
        return [string_to_float(i[len(i) - 4].string) for i in table]
    
    def get_instructor_ratings(source):
        # Gather instructor rating means
        ratings = source
        table = ratings.find_all("tr", attrs={"class": "CondensedTabularOddRows"})
        table = [i.contents for i in table]
        return [string_to_float(i[len(i) - 4].string) for i in table]
    
    def get_workload_mean(source):
        # Gather workload mean
        workload = source
        table = workload.find_all("tbody")
        return [string_to_float(table[0].contents[3].find("td", attrs={"class": "TabularBody_RightColumn_NoWrap"}).string)]
    
    def get_recommendability_mean(source):
        # Gather recommendability mean
        recommend = source
        table = recommend.find_all("tbody")
        return [string_to_float(table[1].contents[2].find("td", attrs={"class": "TabularBody_RightColumn_NoWrap"}).string)]
    
    def get_comment_sentiment(source):
        # Gather comments and run sentiment analysis
        comments = source
        comments = comments.find("tbody").contents
        comments = [i.find("td").string for i in comments if i != '\n']
        sentiment = 0.0
        for comment in comments:
            # Check for null comment
            if not comment:
                continue

            # Initialize model and predict
            s = flair.data.Sentence(comment)
            FLAIR.predict(s)

            # Analyze label
            s = s.to_dict()["all labels"][0]
            if s["value"] == 'NEGATIVE':
                sentiment += -1.0 * s["confidence"]
            else:
                sentiment += 1.0 * s["confidence"]
        sentiment = sentiment / len(comments)
        return [sentiment]

    # Print starting message
    print("SCRAPING NEW QGUIDE DATA...")

    # Begin try-exception branch
    try:
        # Open CSV file as write
        with open(CSV, 'w', newline="") as f:
            # Instantiate CSV file writer
            writer = csv.writer(f)

            # Retrieve term list
            CHROME.get(NEW_URL)
            soup = bs(CHROME.page_source, "html.parser")
            terms = soup.find(id="calTermDropdown").contents
            terms = [i for i in terms if i != '\n'] 

            # Iterate through all terms and scrape
            for term in terms:
                term = term.string
                term_adj = term.replace(" ", "%20")
                term_adj = "&calTerm=" + term_adj

                # Retrieve department list
                CHROME.get(NEW_URL + term_adj)
                soup = bs(CHROME.page_source, "html.parser")
                depts = soup.find_all("div", class_="card p-0")
                
                # Iterate through all the departments and scrape
                for dept in depts:
                    # Retrieve department name
                    dept_name = dept.find("b").string

                    # Retrieve course list and iterate through classes
                    courses = dept.find_all("a")
                    for course in courses:
                        # Gather course info
                        course_url = course.get("href")
                        course_info = course.string
                        course_info = course_info.replace("\n", " ")
                        course_info = course_info.strip()

                        # Parse the string for details
                        idx_dash = course_info.find("-")
                        idx_paren = course_info.find("(")
                        course_name = course_info.split("-")
                        if " " in course_name[0]:
                            course_name = course_name[0]
                        else:
                            course_name = course_name[0] + "-" + course_name[1]
                            idx_dash = len(course_name)
                        course_description = course_info[idx_dash + 1: idx_paren - 1]
                        course_description = course_description.strip()
                        course_instructor = course_info[idx_paren + 1:].strip()
                        course_instructor = course_instructor[:-1]

                        # Retrieve course evaluation page info
                        CHROME.get(course_url)
                        soup = bs(CHROME.page_source, "html.parser")
                        course_evaluations = soup.find_all("div", attrs={"class": "report-block"})
                        course_comments = soup.find("div", attrs={"class": "avoid-page-break-inside"})

                        # Initialize null values
                        c_sum = [course_name, course_description, course_instructor, dept_name, term, course_url]
                        c_res = [float("nan")] * 3
                        c_rat = [float("nan")] * 5
                        c_ins = [float("nan")] * 7
                        c_wor = [float("nan")]
                        c_rec = [float("nan")]
                        c_sen = [float("nan")]

                        # Check for existing page components
                        for eval in course_evaluations:
                            header = eval.find("span").string
                            if header.startswith("Course Response"):
                                c_res = get_course_responses(eval)
                            elif header.startswith("Course General"):
                                c_rat = get_course_ratings(eval)
                            elif header.startswith("General Instructor"):
                                c_ins = get_instructor_ratings(eval)
                            elif header.startswith("On average"):
                                c_wor = get_workload_mean(eval)
                            elif header.startswith("\nHow strongly"):
                                c_rec = get_recommendability_mean(eval)
                        if course_comments:
                            c_sen = get_comment_sentiment(course_comments)
                        else: 
                            c_sen = [float("nan")]
                        
                        # Write data to CSV
                        course_data = c_sum + c_res + c_rat + c_ins + c_wor + c_rec + c_sen
                        writer.writerow(course_data)

                        # Print progress
                        print(repr(course_name), repr(course_description), repr(course_instructor))

        # Return success
        print("SCRAPE SUCCESS.\n")
        return 0
    except:
        # Return failure
        print(traceback.format_exc())
        return 1

######################################## MAIN

if __name__ == "__main__":
    # Authenticate and retrieve login status
    login_status = auth()

    # Status check and scrape data
    if login_status == 0:
        # qscrape_old()
        qscrape_new()

    # Print exit message and quit
    print("PROCESS COMPLETE.")
    CHROME.close()
    quit()