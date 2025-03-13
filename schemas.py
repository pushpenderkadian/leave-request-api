from pydantic import BaseModel, Field
from typing import List,Literal
from datetime import datetime,date

class LeaveRequestCreate(BaseModel):
    employee_id: int = Field(..., example=1)
    leave_type: Literal['ANNUAL', 'SICK', 'PERSONAL'] = Field(..., example='ANNUAL')
    start_date: date = Field(..., example='2022-01-01')
    end_date: date = Field(..., example='2022-01-01')
    reason: str = Field(..., example='Personal Reason',min_length=10)

class LeaveRequestResponse(BaseModel):
    id: int
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: str
    status: str
    working_days: int
    created_at: datetime