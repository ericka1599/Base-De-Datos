import sqlite3
conn = sqlite3.connect('Personas.db')

conn.execute("INSERT INTO Persona(nombre, apellido, edad) VALUES('Ericka', 'Segura' , 17)")
conn.execute("INSERT INTO Persona(nombre, apellido, edad) VALUES('Lilian', 'Bonilla' , 52)")
conn.execute("INSERT INTO Persona(nombre, apellido, edad) VALUES('Marlon', 'Bonilla' , 27)")
conn.execute("INSERT INTO Persona(nombre, apellido, edad) VALUES('Erick', 'Segura' , 53)")

conn.commit()
conn.close()