# Employee Leave Request Management API

## Overview
A FastAPI service for managing employee leave requests with SQLlite

## Features
    -   **Create and retrieve** leave requests
    -   **Business rule Validation** 
    -   **Proper error handling**

## Setup Instrutions

1. **Clone the repository **
    ```sh
    git clone https://github.com/pushpenderkadianleave-request-api.get
    cd leave-request-api
    ```

2. **Create and activate a virtual environment and Install dependencies**
    ```sh
    python -m venv venv
    source venv/bin/activate  #for mac/linux
    venv\Scripts\activate #windows

    pip install -r requirements.txt
    ```

3. **Configure environment variable**
    - Copy `.env.example` to `.env`
    - Update `DATABASE_URL` 

4. **Run the application**
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```


## API Endpoints documentation

### Use Swagger UI : visit /docs path on your domain (if any) or http://127.0.0.1:8000/docs

### Test the endpoints from postman or swagger UI


