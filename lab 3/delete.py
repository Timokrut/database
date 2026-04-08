import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM Crew WHERE crew_id = 2")

conn.commit()
conn.close()