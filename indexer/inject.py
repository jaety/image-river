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
    cmds = []
    for line in lines[:5]:
        hsh = subprocess.check_output(["md5", "-q", line[0]]).strip()
        cmds.append("insert into image_file VALUES ('dummy', '%s', '%s')" % (line[0],hsh))
    schemas.sqlite_execute(db, *cmds)
    with schemas.sqlite_cursor(db) as c:
        c.execute("select * from image_file")
        for row in c.fetchall():
            print row
