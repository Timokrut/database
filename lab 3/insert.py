import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

# companies
cursor.execute("INSERT INTO company (name, country) VALUES ('Air France', 'France')")
cursor.execute("INSERT INTO company (name, country) VALUES ('Turkish Airlines', 'Turkey')")
cursor.execute("INSERT INTO company (name, country) VALUES ('Ryanair', 'Ireland')")

# airports
cursor.execute("INSERT INTO airport (name, city, country) VALUES ('Paris Airport', 'Paris', 'France')")
cursor.execute("INSERT INTO airport (name, city, country) VALUES ('Istanbul Airport', 'Istanbul', 'Turkey')")
cursor.execute("INSERT INTO airport (name, city, country) VALUES ('Frankfurt Airport', 'Frankfurt', 'Germany')")

# flights
cursor.execute("""
INSERT INTO flight (company_id, departure_airport_id, arrival_airport_id, flight_number)
VALUES (1, 1, 2, 'PI123')
""")

cursor.execute("""
INSERT INTO flight (company_id, departure_airport_id, arrival_airport_id, flight_number)
VALUES (2, 2, 3, 'SF456')
""")

# schedule
cursor.execute("""
INSERT INTO schedule (flight_id, departure_datetime, arrival_datetime)
VALUES (1, '2026-03-24 8:00', '2026-03-24 14:00')
""")

cursor.execute("""
INSERT INTO schedule (flight_id, departure_datetime, arrival_datetime)
VALUES (2, '2026-03-24 14:00', '2026-03-24 18:00')
""")

# crew
cursor.execute("""
INSERT INTO crew (company_id, full_name, position)
VALUES (1, 'Jean Dupont', 'Flight Attendant')
""")

cursor.execute("""
INSERT INTO crew (company_id, full_name, position)
VALUES (2, 'Fatma Nur', 'Pilot')
""")

cursor.execute("""
INSERT INTO crew (company_id, full_name, position)
VALUES (3, 'Hans Muller', 'Pilot')
""")


# aircraft
cursor.execute("""
INSERT INTO aircraft (company_id, model, tail_number, capacity)
VALUES (1, 'Airbus A320', 'D-ABCD', 180)
""")

cursor.execute("""
INSERT INTO aircraft (company_id, model, tail_number, capacity)
VALUES (2, 'Boeing 737', 'F-EFGH', 160)
""")

# runway
cursor.execute("""
INSERT INTO runway (airport_id, length_meters, width_meters, amount)
VALUES (1, 4000, 60, 2)
""")

cursor.execute("""
INSERT INTO runway (airport_id, length_meters, width_meters, amount)
VALUES (2, 4200, 70, 3)
""")

conn.commit()
