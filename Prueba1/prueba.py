import sqlite3
conn = sqlite3.connect('personas.db')

#Create Table
conn.execute ("CREATE TABLE Familia (id integer primary key autoincrement, nombre text, apellido text, edad integer )")
conn.execute("CREATE TABLE Persona (id integer primary key autoincrement, familia_id integer, nombre text, apellido text, edad integer, FOREING KEY (familia_id) REFERENCES Familia(id) )")



# #Insert row of data

conn.commit()
conn.close()