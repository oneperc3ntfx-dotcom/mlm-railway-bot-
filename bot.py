import config
from sheets import get_service, read_sheet, write_sheet
from datetime import datetime

def run_bot():

    service = get_service()

    # =========================
    # READ TRANSAKSI
    # =========================
    trx = read_sheet(service, config.GOOGLE_SHEET_ID, "TRANSAKSI")
    owner_db = read_sheet(service, config.OWNER_SHEET_ID, "OWNER")

    # =========================
    # BUILD OWNER MAP (RULE)
    # =========================
    owner_map = {}

    for i in range(1, len(owner_db)):
        row = owner_db[i]

        if len(row) < 3:
            continue

        ref = row[0]
        class_type = row[1]
        sponsor = row[2] if len(row) > 2 else "-"

        owner_map[ref] = {
            "class": class_type,
            "sponsor": sponsor
        }

    # =========================
    # GROUP TRANSAKSI
    # =========================
    data = {}

    for i in range(1, len(trx)):
        row = trx[i]

        try:
            ref = row[6]
            harga = float(row[3])
            date = row[4]

        except:
            continue

        if not ref or "TANGGAL" in ref:
            continue

        if ref not in data:
            data[ref] = {
                "signal": 0,
                "omset": 0,
                "date": date
            }

        data[ref]["signal"] += 1
        data[ref]["omset"] += harga

    # =========================
    # OUTPUT DATA
    # =========================
    owner_output = []
    class1_output = []
    class2_output = []

    total_signal = 0
    total_omset = 0

    for ref, val in data.items():

        total_signal += val["signal"]
        total_omset += val["omset"]

        # OWNER OUTPUT (rekap)
        owner_output.append([
            datetime.now().strftime("%Y-%m-%d"),
            ref,
            val["signal"],
            val["omset"]
        ])

        rule = owner_map.get(ref)

        if not rule:
            continue

        if rule["class"] == "Class 1":
            class1_output.append([
                val["date"],
                ref,
                val["signal"],
                val["omset"]
            ])

        elif rule["class"] == "Class 2":
            class2_output.append([
                val["date"],
                ref,
                val["signal"],
                val["omset"]
            ])

    # TOTAL ROW
    owner_output.append([
        datetime.now().strftime("%Y-%m-%d"),
        "TOTAL KESELURUHAN",
        total_signal,
        total_omset
    ])

    # =========================
    # WRITE OUTPUT
    # =========================
    if owner_output:
        write_sheet(service, config.OWNER_SHEET_ID, "OWNER", owner_output)

    if class1_output:
        write_sheet(service, config.CLASS1_SHEET_ID, "CLASS_1", class1_output)

    if class2_output:
        write_sheet(service, config.CLASS2_SHEET_ID, "CLASS_2", class2_output)
