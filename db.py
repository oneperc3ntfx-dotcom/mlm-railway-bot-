def load_db(raw):
    db = {}

    for row in raw:
        if len(row) < 4:
            continue

        referral = row[0]
        role = row[1]
        sponsor = row[2] if len(row) > 2 else "-"

        db[referral] = {
            "role": role,
            "sponsor": sponsor
        }

    return db
