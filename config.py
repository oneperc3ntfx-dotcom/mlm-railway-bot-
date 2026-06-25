import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
OWNER_SHEET_ID = os.getenv("OWNER_SHEET_ID")
CLASS1_SHEET_ID = os.getenv("CLASS1_SHEET_ID")
CLASS2_SHEET_ID = os.getenv("CLASS2_SHEET_ID")

SERVICE_EMAIL = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
