"""
Utility functions for Q-Guide Plus data processing.
These functions are extracted from qscrape.py to enable unit testing.
"""

import math


def string_to_float(s):
    """
    Convert a string to float, returning NaN if conversion fails.
    
    Args:
        s: String to convert
        
    Returns:
        float: The converted value, or NaN if conversion fails
    """
    try:
        return float(s)
    except (ValueError, TypeError):
        return float("nan")


def get_course_responses(source):
    """
    Extract course response statistics from HTML source.
    
    Args:
        source: BeautifulSoup element containing response data
        
    Returns:
        list: [enrolled_count, eval_count, response_ratio]
    """
    responses = source
    course_enrolled = string_to_float(
        responses.find("td", attrs={"headers": "hdGroup0 InvitedCount"}).string
    )
    course_evals = string_to_float(
        responses.find("td", attrs={"headers": "hdGroup0 RespCount"}).string
    )
    course_ratio = string_to_float(
        str(math.floor((course_evals / course_enrolled) * 100))
    )
    return [course_enrolled, course_evals, course_ratio]


def get_course_ratings(source):
    """
    Extract course rating means from HTML source.
    
    Args:
        source: BeautifulSoup element containing ratings data
        
    Returns:
        list: List of 5 course rating values
    """
    ratings = source
    table = ratings.find_all("tr", attrs={"class": "CondensedTabularOddRows"})
    table = [i.contents for i in table]
    return [string_to_float(i[len(i) - 4].string) for i in table]


def get_instructor_ratings(source):
    """
    Extract instructor rating means from HTML source.
    
    Args:
        source: BeautifulSoup element containing instructor ratings data
        
    Returns:
        list: List of 7 instructor rating values
    """
    ratings = source
    table = ratings.find_all("tr", attrs={"class": "CondensedTabularOddRows"})
    table = [i.contents for i in table]
    return [string_to_float(i[len(i) - 4].string) for i in table]


def get_workload_mean(source):
    """
    Extract workload mean from HTML source.
    
    Args:
        source: BeautifulSoup element containing workload data
        
    Returns:
        list: [workload_mean]
    """
    workload = source
    table = workload.find_all("tbody")
    return [
        string_to_float(
            table[0]
            .contents[3]
            .find("td", attrs={"class": "TabularBody_RightColumn_NoWrap"})
            .string
        )
    ]


def get_recommendability_mean(source):
    """
    Extract recommendability mean from HTML source.
    
    Args:
        source: BeautifulSoup element containing recommendability data
        
    Returns:
        list: [recommendability_mean]
    """
    recommend = source
    table = recommend.find_all("tbody")
    return [
        string_to_float(
            table[1]
            .contents[2]
            .find("td", attrs={"class": "TabularBody_RightColumn_NoWrap"})
            .string
        )
    ]


def parse_course_info(course_info):
    """
    Parse course information string into components.
    
    Args:
        course_info: Raw course info string from QGuide
        
    Returns:
        tuple: (course_name, course_description, course_instructor)
    """
    course_info = course_info.replace("\n", " ")
    course_info = course_info.strip()

    idx_dash = course_info.find("-")
    idx_paren = course_info.find("(")
    course_name = course_info.split("-")
    
    if " " in course_name[0]:
        course_name = course_name[0]
    else:
        course_name = course_name[0] + "-" + course_name[1]
        idx_dash = len(course_name)
    
    course_description = course_info[idx_dash + 1 : idx_paren - 1]
    course_description = course_description.strip()
    course_instructor = course_info[idx_paren + 1 :].strip()
    course_instructor = course_instructor[:-1]
    
    return course_name, course_description, course_instructor


def build_course_document(row):
    """
    Build a MongoDB course document from a CSV row.
    
    Args:
        row: List of values from CSV row (24 fields)
        
    Returns:
        dict: Course document ready for MongoDB insertion
    """
    return {
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
