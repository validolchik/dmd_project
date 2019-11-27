from faker import Faker
import psycopg2
import random

con = psycopg2.connect(
	dbname = "hospital",
	user = "postgres",
	password = "postgres",
	host = "localhost",
	port = "60631"
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

cur.execute("delete from person;")
ssn, address, name, surname, date_of_birth, sex = \
            fake.itin(), fake.address(), fake.first_name_male(), \
            fake.last_name_male(), fake.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=115), 'm'

address = address.replace("\n", ", ")
query = "INSERT INTO person (ssn, address, name, surname, date_of_birth, sex) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s') RETURNING person_id;" % \
		(ssn, address, name, surname, date_of_birth, sex)
cur.execute(query)
value = cur.fetchone()[0]
print(value)


# Make the changes to the database persistent
con.commit()
cur.close()
con.close()