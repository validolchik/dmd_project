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

cur.execute("delete from person;")
ssn, address, name, surname, date_of_birth, sex = \
        fake.itin(), fake.address(), fake.first_name_male(), \
        fake.last_name_male(), fake.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=115), 'm'

address = address.replace("\n", ", ")
query_person = "INSERT INTO person (ssn, address, name, surname, date_of_birth, sex) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s') RETURNING person_id;"
cur.execute(query_person, (ssn, address, name, surname, date_of_birth, sex))
query_person = query_person % (ssn, address, name, surname, date_of_birth, sex)
print(query_person)

# Make the changes to the database persistent
con.commit()
cur.close()
con.close()