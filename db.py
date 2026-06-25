def load_db(rows):
    db = {}

    for r in rows:
        if len(r) < 3:
            continue

        referral = r[0].strip()
        cls = r[1].strip()
        sponsor = r[2].strip()

        db[referral] = {
            "class": cls,
            "sponsor": sponsor
        }

    return db
