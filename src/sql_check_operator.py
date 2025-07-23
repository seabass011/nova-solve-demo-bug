"""
SQLCheckOperator - Simplified version with dict validation bug from Airflow 2.7.1
"""

class AirflowException(Exception):
    """Base exception for Airflow"""
    pass


class SQLCheckOperator:
    """
    Performs checks against a database using SQL queries.
    The bug: when records is a dict, `not all(records)` checks keys not values!
    """
    
    def __init__(self, sql: str):
        self.sql = sql
    
    def execute(self, records):
        """Execute the SQL check"""
        print(f"[INFO] Executing SQL check: {self.sql}")
        print(f"[INFO] Record: {records}")
        
        if not records:
            raise AirflowException("Test failed. Query returned no rows.")
        elif not all(records):  # BUG: For dicts, this checks keys not values!
            raise AirflowException(f"Test failed. Query returned {records!r}")
        
        print("[INFO] Success.")
        return "Success"
