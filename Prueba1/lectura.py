import sqlite3
conn = sqlite3.connect('Personas.db')

resultados = conn.execute("SELECT * FROM Familia ORDER BY id DESC")

for resultado in resultados:
	print (resultado)

conn.commit()
conn.close()