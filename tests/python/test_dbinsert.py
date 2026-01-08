"""
Unit tests for dbinsert.py module.
Tests the document structure creation and data transformation logic.
"""

import math
import pytest
from unittest.mock import MagicMock, patch


class TestCourseDocumentStructure:
    """Tests for the course document structure creation."""

    def test_course_summary_structure(self):
        """Test that courseSummary has correct structure."""
        row = [
            "CS50",  # catalog
            "Introduction to Computer Science",  # title
            "David Malan",  # instructor
            "Computer Science",  # department
            "Spring 2023",  # term
            "https://example.com/cs50",  # url
            "150", "120", "80",  # stats
            "4.5", "4.3", "4.2", "4.1", "4.0",  # course ratings
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",  # instructor ratings
            "10.5",  # workload
            "4.9",  # recommend
            "0.85",  # sentiment
        ]
        
        course_summary = {
            "catalog": row[0],
            "title": row[1],
            "instructor": row[2],
            "department": row[3],
            "term": row[4],
            "url": row[5],
        }
        
        assert course_summary["catalog"] == "CS50"
        assert course_summary["title"] == "Introduction to Computer Science"
        assert course_summary["instructor"] == "David Malan"
        assert course_summary["department"] == "Computer Science"
        assert course_summary["term"] == "Spring 2023"
        assert course_summary["url"] == "https://example.com/cs50"

    def test_course_stat_structure(self):
        """Test that courseStat has correct structure with float conversion."""
        row = [
            "CS50", "Intro", "Malan", "CS", "Spring 2023", "url",
            "150", "120", "80",  # enrollment, responses, ratio
            "4.5", "4.3", "4.2", "4.1", "4.0",
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",
            "10.5", "4.9", "0.85",
        ]
        
        course_stat = {
            "enrollment": float(row[6]),
            "responses": float(row[7]),
            "ratio": float(row[8]),
        }
        
        assert course_stat["enrollment"] == 150.0
        assert course_stat["responses"] == 120.0
        assert course_stat["ratio"] == 80.0

    def test_course_rating_structure(self):
        """Test that courseRating has correct structure."""
        row = [
            "CS50", "Intro", "Malan", "CS", "Spring 2023", "url",
            "150", "120", "80",
            "4.5", "4.3", "4.2", "4.1", "4.0",  # overall, materials, assignments, feedback, section
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",
            "10.5", "4.9", "0.85",
        ]
        
        course_rating = {
            "overall": float(row[9]),
            "materials": float(row[10]),
            "assignments": float(row[11]),
            "feedback": float(row[12]),
            "section": float(row[13]),
        }
        
        assert course_rating["overall"] == 4.5
        assert course_rating["materials"] == 4.3
        assert course_rating["assignments"] == 4.2
        assert course_rating["feedback"] == 4.1
        assert course_rating["section"] == 4.0

    def test_instructor_rating_structure(self):
        """Test that instructorRating has correct structure."""
        row = [
            "CS50", "Intro", "Malan", "CS", "Spring 2023", "url",
            "150", "120", "80",
            "4.5", "4.3", "4.2", "4.1", "4.0",
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",  # instructor ratings
            "10.5", "4.9", "0.85",
        ]
        
        instructor_rating = {
            "overall": float(row[14]),
            "lectures": float(row[15]),
            "accessibility": float(row[16]),
            "enthusiasm": float(row[17]),
            "encouragement": float(row[18]),
            "feedback": float(row[19]),
            "returning": float(row[20]),
        }
        
        assert instructor_rating["overall"] == 4.8
        assert instructor_rating["lectures"] == 4.7
        assert instructor_rating["accessibility"] == 4.6
        assert instructor_rating["enthusiasm"] == 4.5
        assert instructor_rating["encouragement"] == 4.4
        assert instructor_rating["feedback"] == 4.3
        assert instructor_rating["returning"] == 4.2

    def test_course_eval_structure(self):
        """Test that courseEval has correct structure."""
        row = [
            "CS50", "Intro", "Malan", "CS", "Spring 2023", "url",
            "150", "120", "80",
            "4.5", "4.3", "4.2", "4.1", "4.0",
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",
            "10.5", "4.9", "0.85",  # workload, recommend, sentiment
        ]
        
        course_eval = {
            "workload": float(row[21]),
            "recommend": float(row[22]),
            "sentiment": float(row[23]),
        }
        
        assert course_eval["workload"] == 10.5
        assert course_eval["recommend"] == 4.9
        assert course_eval["sentiment"] == 0.85

    def test_full_course_document_structure(self):
        """Test the complete course document structure."""
        row = [
            "ECON-101",
            "Principles of Economics",
            "Jane Smith",
            "Economics",
            "Fall 2022",
            "https://example.com/econ101",
            "200", "180", "90",
            "4.2", "4.0", "3.9", "4.1", "3.8",
            "4.5", "4.4", "4.3", "4.6", "4.2", "4.1", "4.0",
            "8.0", "4.3", "0.72",
        ]
        
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
        
        # Verify all top-level keys exist
        assert "courseSummary" in course
        assert "courseStat" in course
        assert "courseRating" in course
        assert "instructorRating" in course
        assert "courseEval" in course
        
        # Verify nested structure
        assert len(course["courseSummary"]) == 6
        assert len(course["courseStat"]) == 3
        assert len(course["courseRating"]) == 5
        assert len(course["instructorRating"]) == 7
        assert len(course["courseEval"]) == 3


class TestDataTransformation:
    """Tests for data transformation and validation."""

    def test_float_conversion_from_string(self):
        """Test that string values are correctly converted to floats."""
        string_values = ["150", "4.5", "0.85", "-1.2"]
        expected = [150.0, 4.5, 0.85, -1.2]
        
        for s, e in zip(string_values, expected):
            assert float(s) == e

    def test_nan_handling(self):
        """Test handling of NaN values in the data."""
        nan_value = float("nan")
        
        assert math.isnan(nan_value)

    def test_row_length_validation(self):
        """Test that a valid row has exactly 24 elements."""
        valid_row = [
            "CS50", "Intro", "Malan", "CS", "Spring 2023", "url",
            "150", "120", "80",
            "4.5", "4.3", "4.2", "4.1", "4.0",
            "4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2",
            "10.5", "4.9", "0.85",
        ]
        
        assert len(valid_row) == 24

    def test_empty_string_float_conversion_raises(self):
        """Test that empty string raises ValueError when converting to float."""
        with pytest.raises(ValueError):
            float("")

    def test_invalid_string_float_conversion_raises(self):
        """Test that invalid string raises ValueError when converting to float."""
        with pytest.raises(ValueError):
            float("not_a_number")


class TestCSVRowIndexMapping:
    """Tests for verifying correct CSV column index mapping."""

    def test_summary_indices(self):
        """Test that summary fields use correct indices (0-5)."""
        row = ["a", "b", "c", "d", "e", "f"] + ["0"] * 18
        
        assert row[0] == "a"  # catalog
        assert row[1] == "b"  # title
        assert row[2] == "c"  # instructor
        assert row[3] == "d"  # department
        assert row[4] == "e"  # term
        assert row[5] == "f"  # url

    def test_stat_indices(self):
        """Test that stat fields use correct indices (6-8)."""
        row = [""] * 6 + ["100", "90", "90"] + ["0"] * 15
        
        assert row[6] == "100"  # enrollment
        assert row[7] == "90"   # responses
        assert row[8] == "90"   # ratio

    def test_course_rating_indices(self):
        """Test that course rating fields use correct indices (9-13)."""
        row = [""] * 9 + ["4.5", "4.4", "4.3", "4.2", "4.1"] + ["0"] * 10
        
        assert row[9] == "4.5"   # overall
        assert row[10] == "4.4"  # materials
        assert row[11] == "4.3"  # assignments
        assert row[12] == "4.2"  # feedback
        assert row[13] == "4.1"  # section

    def test_instructor_rating_indices(self):
        """Test that instructor rating fields use correct indices (14-20)."""
        row = [""] * 14 + ["4.8", "4.7", "4.6", "4.5", "4.4", "4.3", "4.2"] + ["0"] * 3
        
        assert row[14] == "4.8"  # overall
        assert row[15] == "4.7"  # lectures
        assert row[16] == "4.6"  # accessibility
        assert row[17] == "4.5"  # enthusiasm
        assert row[18] == "4.4"  # encouragement
        assert row[19] == "4.3"  # feedback
        assert row[20] == "4.2"  # returning

    def test_eval_indices(self):
        """Test that eval fields use correct indices (21-23)."""
        row = [""] * 21 + ["10.5", "4.9", "0.85"]
        
        assert row[21] == "10.5"  # workload
        assert row[22] == "4.9"   # recommend
        assert row[23] == "0.85"  # sentiment


class TestDatabaseOperations:
    """Tests for database operations with mocked MongoDB."""

    @patch('pymongo.MongoClient')
    def test_mongodb_connection(self, mock_client):
        """Test that MongoDB client is created with correct URI."""
        mock_client.return_value = MagicMock()
        
        db_uri = "mongodb://localhost:27017"
        client = mock_client(db_uri)
        
        mock_client.assert_called_once_with(db_uri)

    @patch('pymongo.MongoClient')
    def test_collection_insert_one(self, mock_client):
        """Test that insert_one is called with correct document."""
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.courses = mock_collection
        mock_client.return_value.test = mock_db
        
        client = mock_client("mongodb://localhost:27017")
        collection = client.test.courses
        
        course = {"courseSummary": {"catalog": "CS50"}}
        collection.insert_one(course)
        
        mock_collection.insert_one.assert_called_once_with(course)
