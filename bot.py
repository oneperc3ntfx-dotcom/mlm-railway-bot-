from sheets import get_service, read_sheet
import config


def clean_transactions(raw_rows):
    clean_data = []

    for row in raw_rows:

        # skip empty
        if not row:
            continue

        # skip header tanggal
        if str(row[0]).strip().startswith("TANGGAL"):
            continue

        # minimal kolom harus ada (A-G)
        if len(row) < 7:
            continue

        username = str(row[0]).strip()
        user_id = str(row[1]).strip()
        paket = str(row[2]).strip()
        harga = str(row[3]).strip()
        join_date = str(row[4]).strip()
        referral = str(row[6]).strip()

        # skip invalid username
        if username == "" or username.lower() == "tidak ada username":
            continue

        # skip kalau referral kosong
        if referral == "":
            continue

        clean_data.append({
            "username": username,
            "user_id": user_id,
            "paket": paket,
            "harga": float(harga) if harga.replace(".", "").isdigit() else 0,
            "join_date": join_date,
            "referral": referral
        })

    return clean_data


def run_bot():
    service = get_service()

    # 🔥 FIX RANGE PENTING
    raw = read_sheet(
        service,
        config.GOOGLE_SHEET_ID,
        "HASIL REFF GRUP SIGNAL!A:G"
    )

    data = clean_transactions(raw)

    print("TOTAL RAW:", len(raw))
    print("TOTAL CLEAN:", len(data))

    # contoh output debug
    for d in data[:5]:
        print(d)


if __name__ == "__main__":
    run_bot()
