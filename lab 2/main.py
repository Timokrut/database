import sqlite3

conn = sqlite3.connect("airport.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Company (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Airport (
    airport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Flight (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    departure_airport_id INTEGER NOT NULL,
    arrival_airport_id INTEGER NOT NULL,
    flight_number TEXT NOT NULL,

    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (departure_airport_id) REFERENCES Airport(airport_id),
    FOREIGN KEY (arrival_airport_id) REFERENCES Airport(airport_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Schedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_id INTEGER NOT NULL,
    departure_datetime TEXT,
    arrival_datetime TEXT,

    FOREIGN KEY (flight_id) REFERENCES Flight(flight_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Crew (
    crew_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,
    position TEXT,

    FOREIGN KEY (company_id) REFERENCES Company(company_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Aircraft (
    aircraft_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    model TEXT NOT NULL,
    tail_number TEXT NOT NULL,
    capacity INTEGER,

    FOREIGN KEY (company_id) REFERENCES Company(company_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Runway (
    runway_id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_id INTEGER NOT NULL,
    length_meters INTEGER,
    width_meters INTEGER,
    amount INTEGER,

    FOREIGN KEY (airport_id) REFERENCES Airport(airport_id)
)
""")

conn.commit()
conn.close()