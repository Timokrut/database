import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

# Президент в компанию
# cursor.execute("""
# ALTER TABLE company ADD COLUMN President TEXT
# """)

# # Новый аэропорт
# cursor.execute("INSERT INTO airport (name, city, country) VALUES ('Kennedy Airport', 'New York', 'USA')")

# # Удалить самолет
# cursor.execute("""
# DELETE FROM aircraft WHERE aircraft_id = 1
# """)

cursor.execute("UPDATE company SET President = 'POTAPOV TIMOFEI' WHERE company_id = 2")
conn.commit()