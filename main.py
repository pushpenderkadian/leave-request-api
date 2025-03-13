from fastapi import FastAPI
import models.models as models
from db.database import engine
from api.routes import router
from exceptions import ValidationError,validation_exception_handler

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(router,prefix="/api/v1",tags=["leave requests"])

app.get("/")
async def root():
    return {"message":"Leave request system is running"}

app.add_exception_handler(ValidationError,validation_exception_handler)
