def load_db(raw):
    db = {}

    for row in raw:
        if len(row) < 4:
            continue

        referral = row[0].strip()
        kelas = row[1].strip()
        sponsor = row[2].strip()

        db[referral] = {
            "class": kelas,
            "sponsor": sponsor
        }

    return db
