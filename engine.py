from collections import defaultdict


def clean_transactions(rows):
    data = []

    for r in rows:
        if not r:
            continue

        if str(r[0]).startswith("TANGGAL"):
            continue

        try:
            harga = int(str(r[3]).replace(",", ""))
            date = r[4].split(" ")[0]
            referral = r[6]
        except:
            continue

        if not referral:
            continue

        data.append({
            "date": date,
            "referral": referral,
            "harga": harga
        })

    return data


def run_engine(data, db, target_date):
    owner = defaultdict(lambda: {"count": 0, "omset": 0})
    class1 = defaultdict(lambda: {"count": 0, "own": 0, "downline": 0})
    class2 = defaultdict(lambda: {"count": 0, "komisi": 0})

    for d in data:
        if d["date"] != target_date:
            continue

        ref = d["referral"]
        price = d["harga"]

        if ref not in db:
            continue

        cls = db[ref]["class"]
        sponsor = db[ref]["sponsor"]

        # OWNER
        owner[ref]["count"] += 1
        owner[ref]["omset"] += price

        # CLASS 2
        if cls.lower() == "class 2":
            class2[ref]["count"] += 1
            class2[ref]["komisi"] += price

            if sponsor in db:
                class1[sponsor]["downline"] += price

        # CLASS 1
        if cls.lower() == "class 1":
            class1[ref]["count"] += 1
            class1[ref]["own"] += price

    return owner, class1, class2
