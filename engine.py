from collections import defaultdict

def clean_transactions(raw):
    data = []

    for r in raw:
        if len(r) < 7:
            continue

        try:
            data.append({
                "username": r[0],
                "user_id": r[1],
                "paket": r[2],
                "harga": float(str(r[3]).replace(".", "").replace(",", "")),
                "tanggal": r[4],
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

        ref = d["referral"]
        harga = d["harga"]

        if ref not in db:
            continue

        level = db[ref]["class"]
        sponsor = db[ref]["sponsor"]

        # CLASS 2
        if level == "Class 2":
            class2[ref]["count"] += 1
            class2[ref]["komisi"] += harga * 0.3

        # CLASS 1
        elif level == "Class 1":
            class1[ref]["count"] += 1
            class1[ref]["own"] += harga * 0.3

            # sponsor income
            if sponsor in class1:
                class1[sponsor]["downline"] += harga * 0.2

        # OWNER
        elif level == "OWNER":
            owner[ref]["count"] += 1
            owner[ref]["omset"] += harga

    return owner, class1, class2
