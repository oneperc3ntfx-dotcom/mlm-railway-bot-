from sheets import get_service, read_sheet, write_sheet
import config
from engine import clean_transactions, run_engine
from db import load_db
from datetime import datetime


def rupiah(x):
    return "Rp{:,.0f}".format(x).replace(",", ".")


def run_daily():
    service = get_service()

    raw_data = read_sheet(service, config.GOOGLE_SHEET_ID, config.DATA_SHEET)
    raw_db = read_sheet(service, config.GOOGLE_SHEET_ID, config.OWNER_SHEET)

    data = clean_transactions(raw_data)
    db = load_db(raw_db)

    today = datetime.now().strftime("%Y-%m-%d")

    owner, class1, class2 = run_engine(data, db, today)

    # ===== OWNER =====
    owner_rows = [[today, k, v["count"], rupiah(v["omset"])]
                  for k, v in owner.items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.OWNER_SHEET, owner_rows)

    # ===== CLASS 1 =====
    class1_rows = [[today, k, v["count"], rupiah(v["own"]), rupiah(v["downline"])]
                   for k, v in class1.items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.CLASS1_SHEET, class1_rows)

    # ===== CLASS 2 =====
    class2_rows = [[today, k, v["count"], rupiah(v["komisi"])]
                   for k, v in class2.items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.CLASS2_SHEET, class2_rows)

    print("✅ DONE REPORT", today)
