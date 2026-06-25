from sheets import get_service, read_sheet, safe_range
import config


def clean_transactions(raw_rows):
    clean_data = []

    for row in raw_rows:
        if not row:
            continue

        if str(row[0]).strip().upper().startswith("TANGGAL"):
            continue

        if len(row) < 7:
            continue

        username = str(row[0]).strip()
        user_id = str(row[1]).strip()
        paket = str(row[2]).strip()
        harga = str(row[3]).strip()
        join_date = str(row[4]).strip()
        referral = str(row[6]).strip()

        if not username or username.lower() == "tidak ada username":
            continue

        if not referral:
            continue

        try:
            harga_clean = float(harga.replace(",", "").replace(".", "")) if harga else 0
        except:
            harga_clean = 0

        clean_data.append({
            "username": username,
            "user_id": user_id,
            "paket": paket,
            "harga": harga_clean,
            "join_date": join_date,
            "referral": referral
        })

    return clean_data


def run_bot():
    service = get_service()

    sheet_name = "HASIL REFF GRUP SIGNAL"

    range_name = safe_range(sheet_name, "A:G")

    raw = read_sheet(
        service,
        config.GOOGLE_SHEET_ID,
        range_name
    )

    data = clean_transactions(raw)

    print("TOTAL RAW:", len(raw))
    print("TOTAL CLEAN:", len(data))

    for d in data[:5]:
        print(d)


if __name__ == "__main__":
    run_bot()
