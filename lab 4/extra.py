import sqlite3

conn = sqlite3.connect("airport.db")
cursor = conn.cursor()

# все города аэропортов без повторений, отсортированные
# DISTINCT + ORDER BY
print(*cursor.execute("""
SELECT DISTINCT city
FROM Airport
ORDER BY city
"""), sep="\n")

# самолёты, принадлежащие компаниям из России
# IN / NOT IN
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE company_id IN (
    SELECT company_id 
    FROM Company 
    WHERE country = 'Russia'
)
"""), sep="\n")

# самолёты со средней дальностью
# BETWEEN
print(*cursor.execute("""
SELECT model, range_km
FROM Aircraft
WHERE range_km BETWEEN 2500 AND 6000
"""), sep="\n")

# IS NULL
# самолёты без указанной дальности
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE range_km IS NULL
"""), sep="\n")

# самолёты Boeing
# LIKE
print(*cursor.execute("""
SELECT model
FROM Aircraft
WHERE manufacturer LIKE 'Boeing%';
"""), sep="\n")


# средняя дальность самолётов по компаниям
# AVG
print(*cursor.execute("""
SELECT company_id, AVG(range_km)
FROM Aircraft
GROUP BY company_id;
"""), sep="\n")

# самый короткий рейс
# MIN
print(*cursor.execute("""
SELECT MIN(duration_minutes)
FROM Flight;
"""), sep="\n")

# общее количество мест у каждой компании
# SUM
print(*cursor.execute("""
SELECT company_id, SUM(capacity)
FROM Aircraft
GROUP BY company_id;
"""), sep="\n")

### ПОДЗАПРОСЫ ?INSERT UPDATE DELETE?

# заменить NULL значения
# COALESCE
print(*cursor.execute("""
SELECT model, COALESCE(range_km, 0) as range_fixed
FROM Aircraft
"""), sep="\n")

# категория + обработка NULL
# CASE + COALESCE
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