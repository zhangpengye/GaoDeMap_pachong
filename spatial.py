import sqlite3
with sqlite3.connect(":memory:") as conn:
    conn.enable_load_extension(True)
    cur =conn.cursor()
    cur.execute('SELECT load_extension("C:\Program Files\Spatialite32\libsqlite3-0.dll");')