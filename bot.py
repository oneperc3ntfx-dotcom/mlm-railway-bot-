from sheets import get_service, read_sheet
import config


def gs_range(sheet_name, cell_range):
    # SAFE: handle sheet name dengan spasi / karakter khusus
    return f"'{sheet_name}'!{cell_range}"


def clean_transactions(raw_rows):
    clean_data = []

    for row in raw_rows:

        # skip empty row
        if not row:
            continue

        # skip header
        if str(row[0]).strip().upper().startswith("TANGGAL"):
            continue

        # minimal kolom A-G
        if len(row) < 7:
            continue

        username = str(row[0]).strip()
        user_id = str(row[1]).strip()
        paket = str(row[2]).strip()
        harga = str(row[3]).strip()
        join_date = str(row[4]).strip()
        referral = str(row[6]).strip()

        # skip invalid username
        if not username or username.lower() == "tidak ada username":
            continue

        # skip empty referral
        if not referral:
            continue

        # safe convert harga
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

    SHEET_NAME = "HASIL REFF GRUP SIGNAL"

    # SAFE RANGE (FIX UTAMA DI SINI)
    range_ = gs_range(SHEET_NAME, "A:G")

    raw = read_sheet(
        service,
        config.GOOGLE_SHEET_ID,
        range_
    )

    data = clean_transactions(raw)

    print("TOTAL RAW:", len(raw))
    print("TOTAL CLEAN:", len(data))

    # debug sample
    for d in data[:5]:
        print(d)


if __name__ == "__main__":
    run_bot()
