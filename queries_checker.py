from faker import Faker
import psycopg2
import random

con = psycopg2.connect(
	dbname = "hospital",
	user = "postgres",
	password = "postgres",
	host = "localhost",
	port = "49391"
)

cur = con.cursor()
fake = Faker()
# cur.execute("SELECT app_id FROM appointment ORDER BY app_id DESC LIMIT 1;")
# print(int(cur.fetchone()[0]))

# cur.execute("SELECT name, surname FROM doctor;")
# print(cur.fetchone())

# cur.execute("SELECT person_id FROM medic ORDER BY random() LIMIT 1;")
# medic_id = int(cur.fetchone()[0])
# print(medic_id)

# cur.execute("select person_id from medic;")
# arr_medic_id = cur.fetchall()
# print(arr_medic_id)

cur.execute("select chart_id, start_date from medical_chart;")
print(cur.fetchall())

# Make the changes to the database persistent
con.commit()
cur.close()
con.close()