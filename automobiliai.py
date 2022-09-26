import sqlite3

conn = sqlite3.connect("automobiliai.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    automobiliai (
    marke text,
    modelis text,
    spalva text,
    metai integer,
    kaina real
    )""")
id
while True:
    pasirinkimas = int(input("Pasirinkite: \n1 - įvesti, \n2 - ieškoti, \n3 - išeiti"))
    match pasirinkimas:
        case 1:
            print("Įveskite automobilį")
            marke = input("Markė: ")
            modelis = input("Modelis:")
            spalva = input("Spalva:")
            metai = int(input("Metai:"))
            kaina = float(input("Kaina:"))
            with conn:
                c.execute(f"INSERT INTO automobiliai VALUES (?, ?, ?, ?, ?)", (marke, modelis, spalva, metai, kaina))
            print("Automobilis įvestas")
        case 2:
            marke = input("Markė: ")
            modelis = input("Modelis:")
            spalva = input("Spalva:")
            metai_nuo = input("Metai nuo:")
            metai_iki = input("Metai iki:")
            kaina_nuo = input("Kaina nuo:")
            kaina_iki = input("Kaina iki:")
            search_tuple = (
                marke + '%' if marke else '%',
                modelis + '%' if modelis else '%',
                spalva + '%' if spalva else '%',
                int(metai_nuo) if metai_nuo else 1900,
                int(metai_iki) if metai_iki else 2025,
                int(kaina_nuo) if kaina_nuo else 0,
                int(kaina_iki) if kaina_iki else 10000000
            )
            search_query = '''
                SELECT * FROM automobiliai
                WHERE
                marke LIKE ?
                AND
                modelis LIKE ?
                AND
                spalva LIKE ?
                AND
                metai BETWEEN ? AND ?
                AND
                kaina BETWEEN ? AND ?
                '''

            with conn:
                c.execute(search_query, search_tuple)
                res = c.fetchall()

            for i in res:
                print(i)
            print(f'\nTotal {len(res)} rows found.')