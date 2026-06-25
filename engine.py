from collections import defaultdict

def clean_transactions(rows):
    data = []

    for r in rows:
        if not r or r[0].upper().startswith("TANGGAL"):
            continue

        if len(r) < 7:
            continue

        try:
            data.append({
                "username": r[0],
                "paket": r[2],
                "harga": float(r[3]),
                "join_date": r[4][:10],
                "referral": r[6]
            })
        except:
            continue

    return data


def run_engine(data, db, today):

    owner = defaultdict(lambda: {"count": 0, "omset": 0})
    class1 = defaultdict(lambda: {"count": 0, "own": 0, "downline": 0})
    class2 = defaultdict(lambda: {"count": 0, "komisi": 0})

    for d in data:
        if today not in d["join_date"]:
            continue

        ref = d["referral"]
        harga = d["harga"]

        if ref not in db:
            continue

        role = db[ref]["role"]
        sponsor = db[ref]["sponsor"]

        # ===== OWNER =====
        owner[ref]["count"] += 1
        owner[ref]["omset"] += harga

        # ===== CLASS 1 =====
        if role == "Class 1":
            class1[ref]["count"] += 1
            class1[ref]["own"] += harga * 0.3
            class1[ref]["downline"] += harga * 0.2

        # ===== CLASS 2 =====
        elif role == "Class 2":
            class2[ref]["count"] += 1
            class2[ref]["komisi"] += harga * 0.3

    return owner, class1, class2
