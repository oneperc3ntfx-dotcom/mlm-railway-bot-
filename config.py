import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

# TRANSAKSI
DATA_SHEET = "'data'!A:G"

# DB REFERRAL (SHEET OWNER)
DB_SHEET = "'OWNER'!A:D"

# OUTPUT SHEETS
OWNER_SHEET = "'OWNER_REPORT'!A:D"
CLASS1_SHEET = "'CLASS_1'!A:E"
CLASS2_SHEET = "'CLASS_2'!A:D"

SERVICE_EMAIL = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
