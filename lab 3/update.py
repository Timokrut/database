import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE company
SET country = 'EU'
WHERE name = 'Ryanair'
""")


cursor.execute("""
UPDATE aircraft
SET capacity = 200
WHERE aircraft_id = 1
""")

conn.commit()