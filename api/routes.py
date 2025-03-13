from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
import models.models as models,schemas,utils.services as services
from db.database import SessionLocal

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/leave-requests",response_model=schemas.LeaveRequestResponse)
def create_leave_request(leave_request:schemas.LeaveRequestCreate,db:Session=Depends(get_db)):
    try:
        return services.create_leave_request(db,leave_request)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.get("/leave-requests/{employee_id}",response_model=list[schemas.LeaveRequestResponse])
def get_leave_requests(employee_id:int,db:Session=Depends(get_db)):
    return services.get_leave_requests_by_employee(db,employee_id)
