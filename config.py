import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

DATA_SHEET = "data"
OWNER_SHEET = "yuri"
CLASS1_SHEET = "CLASS_1"
CLASS2_SHEET = "CLASS_2"

SERVICE_EMAIL = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
