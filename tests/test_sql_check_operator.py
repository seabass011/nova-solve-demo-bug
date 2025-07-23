"""
Test for SQLCheckOperator - demonstrates the dict validation bug
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sql_check_operator import SQLCheckOperator, AirflowException


class TestSQLCheckOperator:
    """Test cases for SQLCheckOperator"""
    
    def test_dict_with_false_value_should_fail(self):
        """
        This test SHOULD pass but currently fails due to the bug.
        When a dict has False values, the operator should raise an exception.
        """
        operator = SQLCheckOperator("SELECT has_duplicates FROM validation")
        
        # This dict represents a validation check that failed (False value)
        # The operator SHOULD raise an exception for this
        with pytest.raises(AirflowException, match="Test failed"):
            operator.execute({'has_duplicates': False})
    
    def test_dict_with_true_value_should_pass(self):
        """This should pass - dict with True value"""
        operator = SQLCheckOperator("SELECT is_valid FROM validation")
        result = operator.execute({'is_valid': True})
        assert result == "Success"
    
    def test_empty_dict_should_fail(self):
        """Empty dict should fail"""
        operator = SQLCheckOperator("SELECT * FROM empty_table")
        with pytest.raises(AirflowException, match="Query returned no rows"):
            operator.execute({})
