
import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()

# with conn:
#     query = """
#     CREATE TABLE IF NOT EXISTS draugai (
#         f_name VARCHAR(50),
#         l_name VARCHAR(50),
#         email VARCHAR(100))
#     """
#
#     c.execute(query)

# with conn:
#     c.execute("INSERT INTO draugai VALUES ('Domantas', 'Rutkauskas', 'd.rutkauskas@imone.lt')")
#     c.execute("INSERT INTO draugai VALUES ('Rimas', 'Radzevičius', 'RR@gmail.com')")

# with conn:
#     c.execute("SELECT * From draugai WHERE l_name LIKE 'R%'")
#     print(c.fetchall())

# with conn:
#     c.execute("UPDATE draugai SET email='naujas.email@aol.com' WHERE l_name='Radzevičius'")

# with conn:
#     c.execute("DELETE from draugai WHERE l_name='Rutkauskas'")

# vardas = input('Įveskite vardą: ')
# pavarde = input('Įveskite pavardę: ')
# email = input('Įveskite email: ')
# with conn:
#     c.execute("INSERT INTO draugai VALUES (?, ?, ?)", (vardas, pavarde, email))

# draugai = [
#     ('Jonas', 'Jonaitis', 'jjonaitis@mail.lt'),
#     ('Petras', 'Miltelis', 'petras@pastas.lt'),
#     ('Inga', 'Guobytė', 'ingag@koksskirtumas.lt')
# ]
#
# with conn:
#     c.executemany("INSERT INTO draugai VALUES(?,?,?)", draugai)


# ids = (1, 3, 5)
#
# with conn:
#     c.execute("SELECT * FROM draugai WHERE rowid IN (?,?,?)", ids)
#     print(c.fetchall())

import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    darbuotojai (
    vardas text,
    pavarde text,
    atlyginimas integer
    )""")

while True:
    print("Įveskite darbuotoją")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde:")
    atlyginimas = int(input("atlyginimas :"))

    with conn:
        c.execute(f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', {atlyginimas})")

    with conn:
        c.execute("SELECT * FROM darbuotojai")
        print(c.fetchall())
