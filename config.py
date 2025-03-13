from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./leave_requests.db")
    DATABASE_URL = "sqlite:///./leave_requests.db"

settings = Settings()