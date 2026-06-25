from collections import defaultdict


def parse_data(rows):
    data = []

    for r in rows:
        if not r or str(r[0]).upper().startswith("TANGGAL"):
            continue

        try:
            username = r[0]
            harga = int(r[3])
            date = r[4].split(" ")[0]
            referral = r[6]
        except:
            continue

        data.append({
            "date": date,
            "referral": referral,
            "harga": harga
        })

    return data


def build_engine(data, db, target_date):
    result = {
        "owner": defaultdict(lambda: {"count": 0, "omset": 0}),
        "class1": defaultdict(lambda: {"count": 0, "own": 0, "downline": 0}),
        "class2": defaultdict(lambda: {"count": 0, "komisi": 0}),
    }

    for d in data:
        if d["date"] != target_date:
            continue

        ref = d["referral"]
        price = d["harga"]

        if ref not in db:
            continue

        cls = db[ref]["class"]
        sponsor = db[ref]["sponsor"]

        # ================= OWNER DIRECT =================
        result["owner"][ref]["count"] += 1
        result["owner"][ref]["omset"] += price

        # ================= CLASS 2 =================
        if cls.lower() == "class 2":
            result["class2"][ref]["count"] += 1
            result["class2"][ref]["komisi"] += price

            # sponsor (class 1)
            if sponsor in db:
                result["class1"][sponsor]["downline"] += price

        # ================= CLASS 1 =================
        if cls.lower() == "class 1":
            result["class1"][ref]["count"] += 1
            result["class1"][ref]["own"] += price

    return result
