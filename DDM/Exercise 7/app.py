import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Fruit_selling",
    user="postgres",
    password="123"
)

cur = conn.cursor()


conn.commit()
cur.close()
conn.close()


import functions 