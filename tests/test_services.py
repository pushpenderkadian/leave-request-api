import pytest
from datetime import datetime
from utils.services import calculate_working_days

def test_calculate_working_days():
    start_date=datetime(2025,3,1)
    end_date=datetime(2025,3,10)

    assert calculate_working_days(start_date,end_date)==8

