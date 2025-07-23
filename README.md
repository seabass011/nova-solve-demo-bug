# SQLCheckOperator Bug Demo

This repository demonstrates a real bug from Apache Airflow 2.7.1.

## The Bug
The SQLCheckOperator has a validation bug where it incorrectly passes when a SQL query returns a dictionary with False values.

## Running Tests
```bash
pytest -v
```

The test `test_dict_with_false_value_should_fail` will fail, demonstrating the bug.
