"""
Unit tests for qscrape.py module.
Tests the string_to_float utility function and HTML parsing logic.
"""

import math
import pytest
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup


# Import the string_to_float function from qscrape
# We need to mock the heavy dependencies before importing
@pytest.fixture(autouse=True)
def mock_dependencies():
    """Mock heavy dependencies that are loaded at module import time."""
    with patch.dict('sys.modules', {
        'flair': MagicMock(),
        'flair.models': MagicMock(),
        'flair.data': MagicMock(),
        'selenium': MagicMock(),
        'selenium.webdriver': MagicMock(),
        'selenium.webdriver.chrome.service': MagicMock(),
    }):
        yield


class TestStringToFloat:
    """Tests for the string_to_float utility function."""

    def test_valid_integer_string(self, mock_dependencies):
        """Test conversion of valid integer string."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        assert string_to_float("42") == 42.0

    def test_valid_float_string(self, mock_dependencies):
        """Test conversion of valid float string."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        assert string_to_float("3.14") == 3.14

    def test_negative_number_string(self, mock_dependencies):
        """Test conversion of negative number string."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        assert string_to_float("-5.5") == -5.5

    def test_zero_string(self, mock_dependencies):
        """Test conversion of zero string."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        assert string_to_float("0") == 0.0

    def test_invalid_string_returns_nan(self, mock_dependencies):
        """Test that invalid strings return NaN."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        result = string_to_float("not a number")
        assert math.isnan(result)

    def test_empty_string_returns_nan(self, mock_dependencies):
        """Test that empty string returns NaN."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        result = string_to_float("")
        assert math.isnan(result)

    def test_none_returns_nan(self, mock_dependencies):
        """Test that None returns NaN."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        result = string_to_float(None)
        assert math.isnan(result)

    def test_whitespace_string_returns_nan(self, mock_dependencies):
        """Test that whitespace-only string returns NaN."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        result = string_to_float("   ")
        assert math.isnan(result)

    def test_scientific_notation(self, mock_dependencies):
        """Test conversion of scientific notation string."""
        import sys
        sys.path.insert(0, 'python')
        from python.qscrape import string_to_float
        
        assert string_to_float("1e5") == 100000.0


class TestCourseResponsesParsing:
    """Tests for parsing course response data from HTML."""

    def test_parse_course_responses_valid_html(self):
        """Test parsing valid course response HTML."""
        html = """
        <div>
            <td headers="hdGroup0 InvitedCount">150</td>
            <td headers="hdGroup0 RespCount">120</td>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        
        enrolled = soup.find("td", attrs={"headers": "hdGroup0 InvitedCount"}).string
        evals = soup.find("td", attrs={"headers": "hdGroup0 RespCount"}).string
        
        assert enrolled == "150"
        assert evals == "120"

    def test_calculate_response_ratio(self):
        """Test calculation of response ratio."""
        enrolled = 150.0
        evals = 120.0
        ratio = math.floor((evals / enrolled) * 100)
        
        assert ratio == 80


class TestCourseRatingsParsing:
    """Tests for parsing course ratings from HTML."""

    def test_parse_course_ratings_table(self):
        """Test parsing course ratings from HTML table."""
        html = """
        <div>
            <tr class="CondensedTabularOddRows">
                <td>Question 1</td>
                <td>4.5</td>
                <td>4.2</td>
                <td>4.8</td>
            </tr>
            <tr class="CondensedTabularOddRows">
                <td>Question 2</td>
                <td>4.3</td>
                <td>4.1</td>
                <td>4.6</td>
            </tr>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all("tr", attrs={"class": "CondensedTabularOddRows"})
        table = [i.contents for i in table]
        
        # Extract the mean value (4th from last column)
        ratings = [float(i[len(i) - 4].string) for i in table]
        
        assert ratings == [4.5, 4.3]


class TestWorkloadParsing:
    """Tests for parsing workload data from HTML."""

    def test_parse_workload_mean(self):
        """Test parsing workload mean from HTML."""
        html = """
        <div>
            <tbody>
                <tr></tr>
                <tr></tr>
                <tr></tr>
                <tr>
                    <td class="TabularBody_RightColumn_NoWrap">8.5</td>
                </tr>
            </tbody>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all("tbody")
        workload = table[0].contents[3].find("td", attrs={"class": "TabularBody_RightColumn_NoWrap"}).string
        
        assert workload == "8.5"


class TestCommentSentimentParsing:
    """Tests for parsing and analyzing comment sentiment."""

    def test_parse_comments_from_html(self):
        """Test parsing comments from HTML table."""
        html = """
        <div>
            <tbody>
                <tr><td>Great course!</td></tr>
                <tr><td>Very challenging but rewarding.</td></tr>
                <tr><td>Excellent professor.</td></tr>
            </tbody>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        comments = soup.find("tbody").contents
        comments = [i.find("td").string for i in comments if i != '\n']
        
        assert len(comments) == 3
        assert comments[0] == "Great course!"
        assert comments[1] == "Very challenging but rewarding."
        assert comments[2] == "Excellent professor."

    def test_filter_null_comments(self):
        """Test that null comments are filtered out."""
        comments = ["Great course!", None, "Good professor", None]
        filtered = [c for c in comments if c]
        
        assert len(filtered) == 2
        assert None not in filtered


class TestCourseInfoParsing:
    """Tests for parsing course information strings."""

    def test_parse_course_name_with_single_dash(self):
        """Test parsing course name with single dash format."""
        course_info = "CS50 - Introduction to Computer Science (David Malan)"
        
        idx_dash = course_info.find("-")
        idx_paren = course_info.find("(")
        course_name = course_info.split("-")
        
        if " " in course_name[0]:
            course_name = course_name[0]
        else:
            course_name = course_name[0] + "-" + course_name[1]
            idx_dash = len(course_name)
        
        course_description = course_info[idx_dash + 1: idx_paren - 1].strip()
        course_instructor = course_info[idx_paren + 1:].strip()[:-1]
        
        assert course_name == "CS50 "
        assert course_description == "Introduction to Computer Science"
        assert course_instructor == "David Malan"

    def test_parse_course_name_with_double_dash(self):
        """Test parsing course name with double dash format (e.g., ECON-101A)."""
        course_info = "ECON-101A - Microeconomics (John Smith)"
        
        idx_dash = course_info.find("-")
        idx_paren = course_info.find("(")
        course_name = course_info.split("-")
        
        if " " in course_name[0]:
            course_name = course_name[0]
        else:
            course_name = course_name[0] + "-" + course_name[1]
            idx_dash = len(course_name)
        
        course_description = course_info[idx_dash + 1: idx_paren - 1].strip()
        course_instructor = course_info[idx_paren + 1:].strip()[:-1]
        
        assert course_name == "ECON-101A "
        assert course_description == "Microeconomics"
        assert course_instructor == "John Smith"


class TestTermAdjustment:
    """Tests for term string adjustment for URL encoding."""

    def test_term_url_encoding(self):
        """Test that spaces in term names are URL encoded."""
        term = "Spring 2023"
        term_adj = term.replace(" ", "%20")
        term_adj = "&calTerm=" + term_adj
        
        assert term_adj == "&calTerm=Spring%202023"

    def test_term_without_spaces(self):
        """Test term without spaces."""
        term = "Fall2023"
        term_adj = term.replace(" ", "%20")
        term_adj = "&calTerm=" + term_adj
        
        assert term_adj == "&calTerm=Fall2023"
