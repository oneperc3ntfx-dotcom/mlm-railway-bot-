import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

DATA_SHEET = "data!A:G"
DB_SHEET = "owner_db!A:D"

OWNER_SHEET = "owner!A:D"
CLASS1_SHEET = "class_1!A:E"
CLASS2_SHEET = "class_2!A:D"

SERVICE_EMAIL = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")

PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
