"""
Unit tests for Q-Guide Plus utility functions.
"""

import math
import pytest
from bs4 import BeautifulSoup

from utils import (
    string_to_float,
    get_course_responses,
    get_course_ratings,
    get_instructor_ratings,
    get_workload_mean,
    get_recommendability_mean,
    parse_course_info,
    build_course_document,
)


class TestStringToFloat:
    """Tests for string_to_float function."""

    def test_valid_integer_string(self):
        assert string_to_float("42") == 42.0

    def test_valid_float_string(self):
        assert string_to_float("3.14") == 3.14

    def test_negative_number(self):
        assert string_to_float("-5.5") == -5.5

    def test_zero(self):
        assert string_to_float("0") == 0.0

    def test_invalid_string_returns_nan(self):
        result = string_to_float("not a number")
        assert math.isnan(result)

    def test_empty_string_returns_nan(self):
        result = string_to_float("")
        assert math.isnan(result)

    def test_none_returns_nan(self):
        result = string_to_float(None)
        assert math.isnan(result)

    def test_whitespace_string_returns_nan(self):
        result = string_to_float("   ")
        assert math.isnan(result)

    def test_scientific_notation(self):
        assert string_to_float("1e5") == 100000.0


class TestGetCourseResponses:
    """Tests for get_course_responses function."""

    def test_valid_response_data(self):
        html = """
        <div>
            <td headers="hdGroup0 InvitedCount">100</td>
            <td headers="hdGroup0 RespCount">75</td>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 100.0
        assert result[1] == 75.0
        assert result[2] == 75.0  # 75/100 * 100 = 75%

    def test_full_response_rate(self):
        html = """
        <div>
            <td headers="hdGroup0 InvitedCount">50</td>
            <td headers="hdGroup0 RespCount">50</td>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 50.0
        assert result[1] == 50.0
        assert result[2] == 100.0

    def test_low_response_rate(self):
        html = """
        <div>
            <td headers="hdGroup0 InvitedCount">200</td>
            <td headers="hdGroup0 RespCount">20</td>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_responses(soup)
        assert result[0] == 200.0
        assert result[1] == 20.0
        assert result[2] == 10.0  # 20/200 * 100 = 10%


class TestGetCourseRatings:
    """Tests for get_course_ratings function."""

    def test_valid_ratings(self):
        html = """
        <table>
            <tr class="CondensedTabularOddRows">
                <td>Q1</td><td>4.5</td><td>extra</td><td>extra</td>
            </tr>
            <tr class="CondensedTabularOddRows">
                <td>Q2</td><td>4.2</td><td>extra</td><td>extra</td>
            </tr>
        </table>
        """
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_ratings(soup)
        assert len(result) == 2
        assert result[0] == 4.5
        assert result[1] == 4.2

    def test_empty_table(self):
        html = "<table></table>"
        soup = BeautifulSoup(html, "html.parser")
        result = get_course_ratings(soup)
        assert result == []


class TestGetInstructorRatings:
    """Tests for get_instructor_ratings function."""

    def test_valid_instructor_ratings(self):
        html = """
        <table>
            <tr class="CondensedTabularOddRows">
                <td>Overall</td><td>4.8</td><td>extra</td><td>extra</td>
            </tr>
            <tr class="CondensedTabularOddRows">
                <td>Lectures</td><td>4.6</td><td>extra</td><td>extra</td>
            </tr>
            <tr class="CondensedTabularOddRows">
                <td>Accessibility</td><td>4.9</td><td>extra</td><td>extra</td>
            </tr>
        </table>
        """
        soup = BeautifulSoup(html, "html.parser")
        result = get_instructor_ratings(soup)
        assert len(result) == 3
        assert result[0] == 4.8
        assert result[1] == 4.6
        assert result[2] == 4.9


class TestGetWorkloadMean:
    """Tests for get_workload_mean function."""

    def test_valid_workload(self):
        html = """<div><tbody><tr></tr><tr></tr><tr></tr><tr><td class="TabularBody_RightColumn_NoWrap">8.5</td></tr></tbody></div>"""
        soup = BeautifulSoup(html, "html.parser")
        result = get_workload_mean(soup)
        assert len(result) == 1
        assert result[0] == 8.5


class TestGetRecommendabilityMean:
    """Tests for get_recommendability_mean function."""

    def test_valid_recommendability(self):
        html = """<div><tbody><tr></tr></tbody><tbody><tr></tr><tr></tr><tr><td class="TabularBody_RightColumn_NoWrap">4.3</td></tr></tbody></div>"""
        soup = BeautifulSoup(html, "html.parser")
        result = get_recommendability_mean(soup)
        assert len(result) == 1
        assert result[0] == 4.3


class TestParseCourseInfo:
    """Tests for parse_course_info function."""

    def test_standard_course_format(self):
        course_info = "CS50 - Introduction to Computer Science (David Malan)"
        name, desc, instructor = parse_course_info(course_info)
        assert name == "CS50 "
        assert desc == "Introduction to Computer Science"
        assert instructor == "David Malan"

    def test_course_with_hyphenated_code(self):
        course_info = "ECON-101 - Principles of Economics (John Smith)"
        name, desc, instructor = parse_course_info(course_info)
        assert name == "ECON-101 "
        assert desc == "Principles of Economics"
        assert instructor == "John Smith"

    def test_course_with_newlines(self):
        course_info = "\n  CS50 - Introduction to Computer Science (David Malan)  \n"
        name, desc, instructor = parse_course_info(course_info)
        assert name == "CS50 "
        assert desc == "Introduction to Computer Science"
        assert instructor == "David Malan"

    def test_course_with_multiple_instructors(self):
        course_info = "MATH-21A - Multivariable Calculus (Jane Doe, John Smith)"
        name, desc, instructor = parse_course_info(course_info)
        assert name == "MATH-21A "
        assert desc == "Multivariable Calculus"
        assert instructor == "Jane Doe, John Smith"


class TestBuildCourseDocument:
    """Tests for build_course_document function."""

    def test_valid_row(self):
        row = [
            "CS50",  # catalog
            "Intro to CS",  # title
            "David Malan",  # instructor
            "Computer Science",  # department
            "Fall 2023",  # term
            "https://example.com",  # url
            "500",  # enrollment
            "400",  # responses
            "80",  # ratio
            "4.5",  # overall rating
            "4.3",  # materials
            "4.4",  # assignments
            "4.2",  # feedback
            "4.1",  # section
            "4.8",  # instructor overall
            "4.7",  # lectures
            "4.6",  # accessibility
            "4.9",  # enthusiasm
            "4.5",  # encouragement
            "4.4",  # instructor feedback
            "4.3",  # returning
            "10.5",  # workload
            "4.6",  # recommend
            "0.75",  # sentiment
        ]
        result = build_course_document(row)

        assert result["courseSummary"]["catalog"] == "CS50"
        assert result["courseSummary"]["title"] == "Intro to CS"
        assert result["courseSummary"]["instructor"] == "David Malan"
        assert result["courseSummary"]["department"] == "Computer Science"
        assert result["courseSummary"]["term"] == "Fall 2023"
        assert result["courseSummary"]["url"] == "https://example.com"

        assert result["courseStat"]["enrollment"] == 500.0
        assert result["courseStat"]["responses"] == 400.0
        assert result["courseStat"]["ratio"] == 80.0

        assert result["courseRating"]["overall"] == 4.5
        assert result["courseRating"]["materials"] == 4.3
        assert result["courseRating"]["assignments"] == 4.4
        assert result["courseRating"]["feedback"] == 4.2
        assert result["courseRating"]["section"] == 4.1

        assert result["instructorRating"]["overall"] == 4.8
        assert result["instructorRating"]["lectures"] == 4.7
        assert result["instructorRating"]["accessibility"] == 4.6
        assert result["instructorRating"]["enthusiasm"] == 4.9
        assert result["instructorRating"]["encouragement"] == 4.5
        assert result["instructorRating"]["feedback"] == 4.4
        assert result["instructorRating"]["returning"] == 4.3

        assert result["courseEval"]["workload"] == 10.5
        assert result["courseEval"]["recommend"] == 4.6
        assert result["courseEval"]["sentiment"] == 0.75

    def test_document_structure(self):
        row = ["a"] * 6 + ["1.0"] * 18
        result = build_course_document(row)

        assert "courseSummary" in result
        assert "courseStat" in result
        assert "courseRating" in result
        assert "instructorRating" in result
        assert "courseEval" in result

    def test_numeric_conversion(self):
        row = ["a"] * 6 + ["0"] * 18
        result = build_course_document(row)

        assert isinstance(result["courseStat"]["enrollment"], float)
        assert isinstance(result["courseRating"]["overall"], float)
        assert isinstance(result["instructorRating"]["overall"], float)
        assert isinstance(result["courseEval"]["workload"], float)
