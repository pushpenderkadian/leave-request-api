from fastapi import HTTPException
from fastapi.responses import JSONResponse

class ValidationError(HTTPException):
    def __init__(self, detail = list):
        super().__init__(status_code=400, detail={
            'error': 'Validation_Error',
            'message': 'Invalid request',
            'detail': detail
        })

def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=exc.detail
    )