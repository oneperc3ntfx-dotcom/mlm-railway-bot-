from sheets import get_service, read_sheet, write_sheet
import config
from engine import parse_data, build_engine
from db import load_db
from datetime import datetime


def rupiah(x):
    return "Rp{:,.0f}".format(x).replace(",", ".")


def run_daily():
    service = get_service()

    raw_data = read_sheet(service, config.GOOGLE_SHEET_ID, config.DATA_SHEET)
    raw_db = read_sheet(service, config.GOOGLE_SHEET_ID, config.DB_SHEET)

    data = parse_data(raw_data)
    db = load_db(raw_db)

    today = datetime.now().strftime("%Y-%m-%d")

    result = build_engine(data, db, today)

    # ================= OWNER =================
    owner_rows = [[today, k, v["count"], rupiah(v["omset"])]
                  for k, v in result["owner"].items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.OWNER_SHEET, owner_rows)

    # ================= CLASS 1 =================
    class1_rows = [[today, k, v["count"], rupiah(v["own"]), rupiah(v["downline"])]
                    for k, v in result["class1"].items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.CLASS1_SHEET, class1_rows)

    # ================= CLASS 2 =================
    class2_rows = [[today, k, v["count"], rupiah(v["komisi"])]
                    for k, v in result["class2"].items()]

    write_sheet(service, config.GOOGLE_SHEET_ID, config.CLASS2_SHEET, class2_rows)

    print("✅ REPORT DONE", today)
