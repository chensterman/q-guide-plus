import math
import pytest
from bs4 import BeautifulSoup
from unittest.mock import MagicMock

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import (
    string_to_float,
    get_course_responses,
    get_course_ratings,
    get_instructor_ratings,
    get_workload_mean,
    get_recommendability_mean,
    parse_course_info,
    create_course_document,
    extract_unique_departments,
)


class TestStringToFloat:
    def test_valid_integer(self):
        assert string_to_float("42") == 42.0

    def test_valid_float(self):
        assert string_to_float("3.14") == 3.14

    def test_negative_number(self):
        assert string_to_float("-5.5") == -5.5

    def test_zero(self):
        assert string_to_float("0") == 0.0

    def test_invalid_string(self):
        result = string_to_float("invalid")
        assert math.isnan(result)

    def test_empty_string(self):
        result = string_to_float("")
        assert math.isnan(result)

    def test_none_value(self):
        result = string_to_float(None)
        assert math.isnan(result)

    def test_whitespace_string(self):
        assert string_to_float("  3.5  ") == 3.5

    def test_scientific_notation(self):
        assert string_to_float("1e10") == 1e10


class TestGetCourseResponses:
    def test_valid_responses(self):
        html = '''
        <div>
            <td headers="hdGroup0 InvitedCount">100</td>
            <td headers="hdGroup0 RespCount">75</td>
        </div>
        '''
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 100.0
        assert result[1] == 75.0
        assert result[2] == 75.0

    def test_low_response_rate(self):
        html = '''
        <div>
            <td headers="hdGroup0 InvitedCount">200</td>
            <td headers="hdGroup0 RespCount">50</td>
        </div>
        '''
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 200.0
        assert result[1] == 50.0
        assert result[2] == 25.0

    def test_full_response_rate(self):
        html = '''
        <div>
            <td headers="hdGroup0 InvitedCount">50</td>
            <td headers="hdGroup0 RespCount">50</td>
        </div>
        '''
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 50.0
        assert result[1] == 50.0
        assert result[2] == 100.0


class TestGetCourseRatings:
    def test_valid_ratings(self):
        html = '<table><tr class="CondensedTabularOddRows"><td>Question 1</td><td>4.5</td><td>extra1</td><td>extra2</td><td>extra3</td></tr><tr class="CondensedTabularOddRows"><td>Question 2</td><td>3.8</td><td>extra1</td><td>extra2</td><td>extra3</td></tr></table>'
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_ratings(soup)
        assert len(result) == 2
        assert result[0] == 4.5
        assert result[1] == 3.8

    def test_empty_ratings(self):
        html = '<table></table>'
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_ratings(soup)
        assert result == []


class TestGetInstructorRatings:
    def test_valid_ratings(self):
        html = '<table><tr class="CondensedTabularOddRows"><td>Instructor Q1</td><td>4.2</td><td>extra1</td><td>extra2</td><td>extra3</td></tr><tr class="CondensedTabularOddRows"><td>Instructor Q2</td><td>4.8</td><td>extra1</td><td>extra2</td><td>extra3</td></tr><tr class="CondensedTabularOddRows"><td>Instructor Q3</td><td>3.9</td><td>extra1</td><td>extra2</td><td>extra3</td></tr></table>'
        soup = BeautifulSoup(html, "html.parser")
        result = get_instructor_ratings(soup)
        assert len(result) == 3
        assert result[0] == 4.2
        assert result[1] == 4.8
        assert result[2] == 3.9


class TestGetWorkloadMean:
    def test_valid_workload(self):
        html = '<div><tbody><tr>row0</tr><tr>row1</tr><tr>row2</tr><tr><td class="TabularBody_RightColumn_NoWrap">8.5</td></tr></tbody></div>'
        soup = BeautifulSoup(html, "html.parser")
        result = get_workload_mean(soup)
        assert result == [8.5]


class TestGetRecommendabilityMean:
    def test_valid_recommendability(self):
        html = '<div><tbody><tr>row0</tr></tbody><tbody><tr>row0</tr><tr>row1</tr><tr><td class="TabularBody_RightColumn_NoWrap">4.2</td></tr></tbody></div>'
        soup = BeautifulSoup(html, "html.parser")
        result = get_recommendability_mean(soup)
        assert result == [4.2]


class TestParseCourseInfo:
    def test_standard_course_format(self):
        course_info = "CS50 - Introduction to Computer Science (David Malan)"
        name, description, instructor = parse_course_info(course_info)
        assert name == "CS50 "
        assert description == "Introduction to Computer Science"
        assert instructor == "David Malan"

    def test_course_with_dash_in_name(self):
        course_info = "ECON-101 - Principles of Economics (John Smith)"
        name, description, instructor = parse_course_info(course_info)
        assert name == "ECON-101 "
        assert description == "Principles of Economics"
        assert instructor == "John Smith"

    def test_course_with_newlines(self):
        course_info = "\nMATH 21A - Multivariable Calculus\n(Jane Doe)\n"
        name, description, instructor = parse_course_info(course_info)
        assert "MATH" in name
        assert "Multivariable Calculus" in description
        assert "Jane Doe" in instructor

    def test_course_with_extra_whitespace(self):
        course_info = "  PHYS 15A - Introductory Mechanics   (Prof. Einstein)  "
        name, description, instructor = parse_course_info(course_info)
        assert "PHYS" in name
        assert "Introductory Mechanics" in description
        assert "Prof. Einstein" in instructor


class TestCreateCourseDocument:
    def test_valid_row(self):
        row = [
            "CS50",
            "Introduction to Computer Science",
            "David Malan",
            "Computer Science",
            "Fall 2023",
            "https://example.com/cs50",
            "500",
            "450",
            "90",
            "4.8",
            "4.5",
            "4.6",
            "4.7",
            "4.4",
            "4.9",
            "4.8",
            "4.7",
            "4.9",
            "4.6",
            "4.5",
            "4.8",
            "10.5",
            "4.7",
            "0.85",
        ]
        result = create_course_document(row)
        
        assert result["courseSummary"]["catalog"] == "CS50"
        assert result["courseSummary"]["title"] == "Introduction to Computer Science"
        assert result["courseSummary"]["instructor"] == "David Malan"
        assert result["courseSummary"]["department"] == "Computer Science"
        assert result["courseSummary"]["term"] == "Fall 2023"
        assert result["courseSummary"]["url"] == "https://example.com/cs50"
        
        assert result["courseStat"]["enrollment"] == 500.0
        assert result["courseStat"]["responses"] == 450.0
        assert result["courseStat"]["ratio"] == 90.0
        
        assert result["courseRating"]["overall"] == 4.8
        assert result["courseRating"]["materials"] == 4.5
        assert result["courseRating"]["assignments"] == 4.6
        assert result["courseRating"]["feedback"] == 4.7
        assert result["courseRating"]["section"] == 4.4
        
        assert result["instructorRating"]["overall"] == 4.9
        assert result["instructorRating"]["lectures"] == 4.8
        assert result["instructorRating"]["accessibility"] == 4.7
        assert result["instructorRating"]["enthusiasm"] == 4.9
        assert result["instructorRating"]["encouragement"] == 4.6
        assert result["instructorRating"]["feedback"] == 4.5
        assert result["instructorRating"]["returning"] == 4.8
        
        assert result["courseEval"]["workload"] == 10.5
        assert result["courseEval"]["recommend"] == 4.7
        assert result["courseEval"]["sentiment"] == 0.85

    def test_document_structure(self):
        row = ["a"] * 6 + ["1.0"] * 18
        result = create_course_document(row)
        
        assert "courseSummary" in result
        assert "courseStat" in result
        assert "courseRating" in result
        assert "instructorRating" in result
        assert "courseEval" in result
        
        assert len(result["courseSummary"]) == 6
        assert len(result["courseStat"]) == 3
        assert len(result["courseRating"]) == 5
        assert len(result["instructorRating"]) == 7
        assert len(result["courseEval"]) == 3


class TestExtractUniqueDepartments:
    def test_unique_departments(self):
        rows = [
            ["", "", "", "Computer Science", "", ""],
            ["", "", "", "Mathematics", "", ""],
            ["", "", "", "Computer Science", "", ""],
            ["", "", "", "Physics", "", ""],
            ["", "", "", "Mathematics", "", ""],
        ]
        result = extract_unique_departments(rows)
        assert result == ["Computer Science", "Mathematics", "Physics"]

    def test_empty_rows(self):
        rows = []
        result = extract_unique_departments(rows)
        assert result == []

    def test_single_department(self):
        rows = [
            ["", "", "", "Economics", "", ""],
            ["", "", "", "Economics", "", ""],
        ]
        result = extract_unique_departments(rows)
        assert result == ["Economics"]

    def test_alphabetical_order(self):
        rows = [
            ["", "", "", "Zoology", "", ""],
            ["", "", "", "Astronomy", "", ""],
            ["", "", "", "Biology", "", ""],
        ]
        result = extract_unique_departments(rows)
        assert result == ["Astronomy", "Biology", "Zoology"]
