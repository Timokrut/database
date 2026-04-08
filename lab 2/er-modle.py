import sqlite3
from eralchemy import render_er

# Прямая генерация ER-диаграммы из SQLite файла
render_er("sqlite:///airport.db", 'airport_er_diagram.png')
