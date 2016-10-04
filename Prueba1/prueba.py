import sqlite3
conn = sqlite3.connect('Personas.db')

#Create Table
conn.execute("CREATE TABLE Persona (id integer primary key autoincrement, nombre text, apellido text, edad integer )")

# #Insert row of data
# conn.execute("INSERT INTO Persona VALUES('Ericka', 'Segura' , 17)")

conn.commit()
conn.close()