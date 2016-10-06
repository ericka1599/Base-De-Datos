import sqlite3
conn = sqlite3.connect('personas.db')

conn.execute("INSERT INTO Persona(nombre, familia_id, apellido, edad) VALUES('Ericka', 1, 17, 'Segura')")
conn.execute("INSERT INTO Persona(nombre, familia_id, apellido, edad) VALUES('Erick', 1, 53, 'Segura')")
conn.execute("INSERT INTO Persona(nombre, familia_id, apellido, edad) VALUES('Lilian', 2, 51, 'Bonilla')")
conn.execute("INSERT INTO Persona(nombre, familia_id, apellido, edad) VALUES('Marlon', 2, 27, 'Bonilla')")

conn.commit()
conn.close()