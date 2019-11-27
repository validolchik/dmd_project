from faker import Faker
import psycopg2
import random

con = psycopg2.connect(
    dbname="hospital",
    user="postgres",
    password="postgres",
    host="localhost",
    port="60631"
)

# http://localhost:60118
cur = con.cursor()
fake = Faker()

file_output = open("inserts.txt", "w+")
file_writing = False

# cur.execute("DELETE FROM appointment;")
# cur.execute("DELETE FROM person;")

def write_into_file(string_query):
    if file_writing:
        file_output.write(string_query + "\n")


# insert male into table person and return query and id of last added person
def create_person_male():
    ssn, address, name, surname, date_of_birth, sex = \
        fake.itin(), fake.address(), fake.first_name_male(), \
        fake.last_name_male(), fake.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=115), 'm'

    address = address.replace("\n", ", ")
    query_person = "INSERT INTO person (ssn, address, name, surname, date_of_birth, sex) \
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING person_id;"
    cur.execute(query_person, (ssn, address, name, surname, date_of_birth, sex))
    query_person = query_person % (ssn, address, name, surname, date_of_birth, sex)
    person_id = cur.fetchone()[0]
    return [query_person, person_id]


# insert female into table person and return query and id of last added person
def create_person_female():
    ssn, address, name, surname, date_of_birth, sex = \
        fake.itin(), fake.address(), fake.first_name_female(), \
        fake.last_name_female(), fake.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=115), 'm'

    address = address.replace("\n", ", ")
    query_person = "INSERT INTO person (ssn, address, name, surname, date_of_birth, sex) \
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING person_id;"
    cur.execute(query_person, (ssn, address, name, surname, date_of_birth, sex))
    query_person = query_person % (ssn, address, name, surname, date_of_birth, sex)
    person_id = cur.fetchone()[0]
    return [query_person, person_id]


# inserting patients
def inserting_patients():
    # cur.execute("DELETE FROM patient;")
    for i in range(25):
        query_id = create_person_male()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)
        query_patient = "INSERT INTO patient (person_id) VALUES (%s);"
        cur.execute(query_patient % person_id)
        write_into_file(query_patient)


    for i in range(25):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)
        query_patient = "INSERT INTO patient (person_id) VALUES (%s);"
        cur.execute(query_patient % person_id)
        write_into_file(query_patient)

# inserting doctors
def inserting_doctors():
    # cur.execute("DELETE FROM doctor;")
    for i in range(12):
        query_id = create_person_male()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)
        
        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=40000, max=80000, step=2000)
        
        query_doctor = "INSERT INTO doctor (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_doctor % (person_id,length_of_service, salary))
        write_into_file(query_doctor)

    for i in range(5):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)
        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=40000, max=80000, step=2000)

        query_doctor = "INSERT INTO doctor (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_doctor % (person_id, length_of_service, salary))
        write_into_file(query_doctor)


# inserting nurses
def inserting_nurses():
    # cur.execute("DELETE FROM nurse;")
    for i in range(10):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)

        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=20000, max=40000, step=2000)

        query_nurse = "INSERT INTO nurse (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_nurse % (person_id, length_of_service, salary))
        write_into_file(query_nurse)


# inserting accountants
def inserting_accountants():
    # cur.execute("DELETE FROM accountant;")
    for i in range(4):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)

        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=20000, max=40000, step=2000)
        
        query_accountant = "INSERT INTO accountant (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_accountant % (person_id, length_of_service, salary))
        write_into_file(query_accountant)

# inserting receptionists
def inserting_receptionists():
    # cur.execute("DELETE FROM receptionist;")
    for i in range(4):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)

        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=20000, max=40000, step=2000)
        
        query_recept = "INSERT INTO receptionist (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_recept % (person_id, length_of_service, salary))
        write_into_file(query_recept)


# inserting storekeepers
def inserting_storekeepers():
    # cur.execute("DELETE FROM storekeeper;")
    for i in range(2):
        query_id = create_person_female()
        query_person = query_id[0]
        person_id = query_id[1]
        write_into_file(query_person)
        length_of_service = fake.random_int(min=3, max=20, step=1)
        salary = fake.random_int(min=20000, max=40000, step=2000)
        query_storekeeper = "INSERT INTO storekeeper (person_id, length_of_service, salary) VALUES (%s, %s, %s);"
        cur.execute(query_storekeeper % (person_id, length_of_service, salary))
        write_into_file(query_storekeeper)

# inserting appointments
def inserting_appointments():
    # cur.execute("DELETE FROM appointment;")
    for i in range(100):
        cur.execute("SELECT person_id FROM patient ORDER BY random() LIMIT 1;")
        patient_id = int(cur.fetchone()[0])

        cur.execute("SELECT person_id FROM receptionist ORDER BY random() LIMIT 1;")
        rec_id = int(cur.fetchone()[0])

        time = fake.date_time_between(start_date="-1d", end_date="now", tzinfo=None)

        query = "INSERT INTO appointment(app_time, room, patient_id, rec_id) VALUES ('%s', '%s', '%s', '%s');"
        cur.execute(query, (time, fake.random_int(min = 1, max = 30, step=1), patient_id, rec_id))
        query = query % (time, fake.random_int(min = 1, max = 30, step=1), patient_id, rec_id)
        write_into_file(query)


# inserting medic_appointments
def inserting_medic_appointments():
    cur.execute("DELETE FROM medic_appointment;")
    cur.execute("SELECT app_id FROM appointment ORDER BY app_id DESC LIMIT 1;")
    last = int(cur.fetchone()[0])
    cur.execute("SELECT app_id FROM appointment LIMIT 1;")
    first = int(cur.fetchone()[0])
    print(first, last)
    for i in range(first, last+1):
        cur.execute("SELECT person_id FROM medic ORDER BY random() LIMIT 1;")
        medic_id = int(cur.fetchone()[0])
        print(medic_id)
        query = "INSERT INTO medic_appointment(app_id, medic_id) VALUES ('%s', '%s');" % \
                (i, medic_id)
        cur.execute(query)
        if file_writing:
            file_output.write(query + "\n")


# inserting medicines
def inserting_medicines():
    cur.execute("DELETE FROM medicine;")
    medicines = ["Dexmedocet", "Prepapiride", "Aggrerotec", "Eprotide",
                 "Aprevance", "Galanpalene", "Oxyconide Butamectin",
                 "Cleoterol Magnesulin", "Romirabine Marvate", "Kiorate Bexlise"]
    for i in range(len(medicines)):
        medicine = random.choice(medicines)
        medicines.remove(medicine)
        price = fake.random_int(min=100, max=500, step=10)
        descr = fake.sentence()
        query = "INSERT INTO medicine(price, name, description) VALUES ('%s', '%s', '%s');" % \
                (price, medicine, descr)
        cur.execute(query)
        if file_writing:
            file_output.write(query + "\n")


# inserting services
def inserting_services():
    cur.execute("DELETE FROM service;")
    services = ["massage"]
    for i in range(len(services)):
        service = random.choice(services)
        services.remove(service)
        price = fake.random_int(min=1000, max=3000, step=500)
        descr = fake.sentence()
        query = "INSERT INTO service(name, description, price) VALUES ('%s', '%s', '%s');" % \
                (service, descr, price)
        cur.execute(query)
        if file_writing:
            file_output.write(query + "\n")


# inserting qualifications
def inserting_qualifications():
    cur.execute("DELETE FROM qualifications;")
    cur.execute("select person_id from medic;")
    arr_medic_id = cur.fetchall()
    qualifications = [fake.word(), fake.word(), fake.word(), fake.word()]
    for medic_id in arr_medic_id:
        n = fake.random_int(min=1, max=len(qualifications), step=1)
        qualifications_set = random.sample(qualifications, n)
        for qualification in qualifications_set:
            query = "INSERT INTO qualifications(descrip, medic_id) VALUES ('%s', '%s');" % \
                    (qualification, medic_id[0])
            cur.execute(query)
            if file_writing:
                file_output.write(query + "\n")


cur.execute("DELETE FROM patient;")
cur.execute("DELETE FROM doctor;")
cur.execute("DELETE FROM nurse;")
cur.execute("DELETE FROM accountant;")
cur.execute("DELETE FROM receptionist;")
cur.execute("DELETE FROM storekeeper;")
cur.execute("DELETE FROM person")
inserting_patients()
inserting_doctors()
inserting_nurses()
inserting_accountants()
inserting_receptionists()
inserting_storekeepers()
inserting_medicines()
inserting_services()
# inserting_appointments()
# inserting_qualifications()

# Make the changes to the database persistent
con.commit()

# Close communication with the database
cur.close()
con.close()

# close file
file_output.close()
