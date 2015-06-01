import schemas
import csv
import hashlib
import subprocess
import os

db = "out/image_info.db"

if os.path.exists(db):
    os.remove(db)
schemas.create(db)

with open("out/image_info.csv") as csvfile:
    reader = csv.reader(csvfile)
    header = reader.next()
    lines = [line for line in reader]
    values = []

    for idx, line in enumerate(lines):
        hsh = subprocess.check_output(["md5", "-q", line[0]]).strip()
        values.append(('jae-laptop', line[0], hsh))
        if idx % 1000 == 0:
            print "%d of %d" % (idx, len(lines))

    schemas.sqlite_executemany(db,
        "insert into image_file VALUES (?,?,?)",
        values
    )
