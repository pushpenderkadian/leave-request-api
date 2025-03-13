from sqlalchemy.orm import Session
import models.models as models,schemas
from datetime import datetime,timedelta
from exceptions import ValidationError

def calculate_working_days(start_date,end_date):
    current_date=start_date
    working_days=0
    while current_date<=end_date:
        if current_date.weekday()<5:
            working_days+=1
        current_date+=timedelta(days=1)
    return working_days

def create_leave_request(db:Session,leave_request:schemas.LeaveRequestCreate):
    errors=[]
    if leave_request.end_date<=leave_request.start_date:
        errors.append('end_date must be after start_date')
    
    working_days=calculate_working_days(leave_request.start_date,leave_request.end_date)
    if working_days>14:
        errors.append("maximum consecutive leave days is 14")
    
    if errors:
        raise ValidationError(detail=errors)
    
    overlapping_request=db.query(models.LeaveRequest).filter(
        models.LeaveRequest.employee_id==leave_request.employee_id,
        models.LeaveRequest.start_date<=leave_request.end_date,
        models.LeaveRequest.end_date>=leave_request.start_date
    ).first()
    if overlapping_request:
        raise ValidationError(detail=["Employee has overlapping leave request"])
    
    new_request = models.LeaveRequest(
        employee_id=leave_request.employee_id,
        start_date=leave_request.start_date,
        end_date=leave_request.end_date,
        leave_type=leave_request.leave_type,
        reason=leave_request.reason,
        working_days=working_days
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def get_leave_requests_by_employee(db:Session,employee_id:int):
    return db.query(models.LeaveRequest).filter(models.LeaveRequest.employee_id==employee_id).all()