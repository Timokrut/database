import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

print("1 список рейсов для заданной авиакомпании")
print(*cursor.execute("SELECT * FROM Flight WHERE company_id = 1"), sep="\n")


print("2 типы самолетов, используемые заданной авиакомпанией")
print(*cursor.execute("SELECT DISTINCT model FROM Aircraft WHERE company_id = 1"), sep="\n")


print("3 авиакомпании, у которых прямой и обратный рейс выполняют различные типы самолетов")
print(*cursor.execute("""
SELECT DISTINCT c.name
FROM Flight f1
JOIN Flight f2 
    ON f1.departure_airport_id = f2.arrival_airport_id
   AND f1.arrival_airport_id = f2.departure_airport_id
   AND f1.company_id = f2.company_id
   AND f1.aircraft_id != f2.aircraft_id
JOIN Company c ON f1.company_id = c.company_id
"""), sep="\n")


print("4 направления, на которых работает более трех авиакомпаний")
print(*cursor.execute("""
SELECT departure_airport_id,
       arrival_airport_id,
       COUNT(DISTINCT company_id) as company_count
FROM Flight
GROUP BY departure_airport_id, arrival_airport_id
HAVING COUNT(DISTINCT company_id) > 3
"""), sep="\n")

print("5 количество авиарейсов, выполняемых между каждой парой аэропортов")
print(*cursor.execute("""
SELECT departure_airport_id,
       arrival_airport_id,
       COUNT(*) as flight_count
FROM Flight
GROUP BY departure_airport_id, arrival_airport_id
"""), sep="\n")

print("6 авиакомпании, выполняющие максимальное количество рейсов")
print(*cursor.execute("""
SELECT c.name
FROM Company c
JOIN Flight f ON c.company_id = f.company_id
GROUP BY c.company_id
HAVING COUNT(f.flight_id) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) as cnt
        FROM Flight
        GROUP BY company_id
    )
)
"""), sep="\n")

print("7 авиакомпании, не работающие в Екатеринбурге")
print(*cursor.execute("""
SELECT c.name
FROM Company c
WHERE c.company_id NOT IN (
    SELECT DISTINCT f.company_id
    FROM Flight f
    JOIN Airport a 
         ON f.departure_airport_id = a.airport_id
         OR f.arrival_airport_id = a.airport_id
    WHERE a.city = 'Екатеринбург'
)
"""), sep="\n")

print("8 авиакомпании, использующие все типы самолетов")
print(*cursor.execute("""
SELECT c.name
FROM Company c
JOIN Aircraft a ON c.company_id = a.company_id
GROUP BY c.company_id
HAVING COUNT(DISTINCT a.model) = (
    SELECT COUNT(DISTINCT model)
    FROM Aircraft
)
"""), sep="\n")

print("9 авиакомпании, у которых все самолеты одного производителя")
print(*cursor.execute("""
SELECT c.name
FROM Company c
JOIN Aircraft a ON c.company_id = a.company_id
GROUP BY c.company_id
HAVING COUNT(DISTINCT a.manufacturer) = 1
"""), sep="\n")

print("""10 самолеты с указанием категории по дальности полета – для
 дальности полета до 2500 км категория самолета «SHORT-HAUL»;
 для дальности полета свыше 6000 км – «LONG-HAUL»; для даль-
 ности полета от 2500 км до 6000 км – «MEDIUM-HAUL»; если даль-
 ность полета меньше 1000 км или не указана, то в категории выве-
 сти «UNDEFINED»""")
print(*cursor.execute("""
SELECT model,
CASE
    WHEN range_km IS NULL OR range_km < 1000 THEN 'UNDEFINED'
    WHEN range_km <= 2500 THEN 'SHORT-HAUL'
    WHEN range_km > 6000 THEN 'LONG-HAUL'
    ELSE 'MEDIUM-HAUL'
END AS category
FROM Aircraft
"""), sep="\n")

print("""11 самолеты с указанием статуса проверки на основе года вы-
 пуска – если самолет выпущен ранее 2010 года, то вывести статус
 «REVIEW_OLD»; если самолет выпущен позже 2010 года, то выве-
 дите статус «NO_REVIEW»;""")
print(*cursor.execute("""
SELECT model,
CASE
    WHEN year_of_production < 2010 THEN 'REVIEW_OLD'
    ELSE 'NO_REVIEW'
END AS review_status
FROM Aircraft
"""), sep="\n")

print("12 самого длительного рейса на основе его продолжительности для авиакомпании «Победа».""")
print(*cursor.execute("""
SELECT f.*
FROM Flight f
JOIN Company c ON f.company_id = c.company_id
WHERE c.name = 'Победа'
ORDER BY f.duration_minutes DESC
LIMIT 1
"""), sep="\n")

conn.commit()
conn.close()