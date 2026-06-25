from googleapiclient.discovery import build
from google.oauth2 import service_account
import config

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_service():
    creds = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "client_email": config.SERVICE_EMAIL,
            "private_key": config.PRIVATE_KEY,
            "token_uri": "https://oauth2.googleapis.com/token"
        },
        scopes=SCOPES
    )
    return build("sheets", "v4", credentials=creds)


def read_sheet(service, sheet_id, range_name):
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()
    return result.get("values", [])


def write_sheet(service, sheet_id, range_name, values):
    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": values}
    ).execute()
