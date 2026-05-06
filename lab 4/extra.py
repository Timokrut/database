import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

# Получить все уникальные модели отсоритированные по вместительности
# DISTINCT + ORDER BY
print(1)
print(*cursor.execute("""
SELECT DISTINCT model, capacity
FROM Aircraft
ORDER BY capacity DESC
"""), sep="\n")

# самолёты, принадлежащие компаниям из России
# IN / NOT IN
print(2)
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE company_id IN (
    SELECT company_id 
    FROM Company 
    WHERE country = 'Россия'
)
"""), sep="\n")

# самолёты со средней дальностью
# BETWEEN
print(3)
print(*cursor.execute("""
SELECT model, range_km
FROM Aircraft
WHERE range_km BETWEEN 2500 AND 6000
"""), sep="\n")

# IS NULL
# самолёты без указанной дальности
print(4)
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE range_km IS NULL
"""), sep="\n")

# самолёты Boeing
# LIKE
print(5)
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE manufacturer LIKE 'Boeing%'
"""), sep="\n")


# средняя дальность самолётов по компаниям
# AVG
print(6)
print(*cursor.execute("""
SELECT company_id, AVG(range_km)
FROM Aircraft
GROUP BY company_id
"""), sep="\n")

# самый короткий рейс
# MIN
print(7)
print(*cursor.execute("""
SELECT MIN(duration_minutes)
FROM Flight
"""), sep="\n")

# общее количество мест у каждой компании
# SUM
print(8)
print(*cursor.execute("""
SELECT c.name, SUM(capacity)
FROM Aircraft a
JOIN Company c ON a.company_id = c.company_id
GROUP BY a.company_id
"""), sep="\n")

#
#
print(9)
print(*cursor.execute("""
UPDATE Aircraft
SET capacity = capacity + 10
WHERE company_id = (
    SELECT company_id
    FROM Flight
    GROUP BY company_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
"""), sep="\n")

# Удалить самолёты, которые ни разу не использовались в рейсах
# DELETE + подзапрос
print(10)
print(*cursor.execute("""
DELETE FROM Aircraft
WHERE aircraft_id NOT IN (
    SELECT DISTINCT aircraft_id
    FROM Flight
)
"""))

# категория + обработка NULL
# CASE + COALESCE
print(11)
print(*cursor.execute("""
SELECT model,
       CASE
           WHEN COALESCE(range_km, 0) < 1000 THEN 'UNDEFINED'
           WHEN range_km <= 2500 THEN 'SHORT'
           ELSE 'OTHER'
       END
FROM Aircraft
"""), sep="\n")

conn.commit()
conn.close()