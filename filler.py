from faker import Faker
import psycopg2
import random

con = psycopg2.connect(
    dbname="hospital",
    user="postgres",
    password="postgres",
    host="localhost",
    port="49391"
)

cur = con.cursor()
fake = Faker()

file_output = open("populate_postgres.sql", "w+")
file_writing = False
number_of_rooms = 20

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
        salary = fake.random_int(min=20000, max=30000, step=2000)

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
    cur.execute("SELECT person_id FROM doctor;")
    doctors_id = cur.fetchall()
    cur.execute("SELECT person_id FROM patient;")
    patients_id = cur.fetchall()
    cur.execute("SELECT person_id FROM nurse;")
    nurses_id = cur.fetchall()
    cur.execute("SELECT person_id FROM receptionist;")
    recs_id = cur.fetchall()

    for doctor in doctors_id:
        for i in range(210):
            room = fake.random_int(min=1, max=number_of_rooms, step=1)
            app_time = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None)

            # cur.execute("SELECT person_id FROM patient ORDER BY random() LIMIT 1;")
            # patient_id = int(cur.fetchone()[0])
            patient_id = random.choice(patients_id)[0]
            nurse_id = random.choice(nurse_id)[0]
            rec_id = random.choice(recs_id)[0]
            doctor_id = doctor[0]

            # cur.execute("SELECT person_id FROM nurse ORDER BY random() LIMIT 1;")
            # nurse_id = int(cur.fetchone()[0])

            # cur.execute("SELECT person_id FROM receptionist ORDER BY random() LIMIT 1;")
            # rec_id = int(cur.fetchone()[0])

            query = "INSERT INTO appointment(app_time, room, patient_id, doctor_id, nurse_id, rec_id) " \
                    "VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(query, (app_time, room, patient_id, doctor_id, nurse_id, rec_id))
            query = query % (app_time, room, patient_id, doctor_id, nurse_id, rec_id)
            write_into_file(query)


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
    services = ["massage", "healing shower", "healing with dirt", "River mud", "Magnetoturbotron", "Prostate massage"]
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


def inserting_medical_charts():
    cur.execute("select person_id from patient;")
    persons = cur.fetchall()
    for person in persons:
        query_date_of_birth = "select date_of_birth from person where person_id=%s;"
        cur.execute(query_date_of_birth % person[0])
        date_of_birth = cur.fetchone()[0]
        date_chart_create = fake.date_time_between(start_date=date_of_birth, end_date="-10y", tzinfo=None)
        query_add_chart = "insert into medical_chart(start_date, chart_id) values (%s, %s);"
        cur.execute(query_add_chart, (date_chart_create, person[0]))
        query_add_chart = query_add_chart % (date_chart_create, person[0])
        write_into_file(query_add_chart)


def inserting_reports():
    cur.execute("select chart_id, start_date from medical_chart;")
    charts = cur.fetchall()

    cur.execute("SELECT person_id FROM doctor;")
    doctors_id = cur.fetchall()

    cur.execute("SELECT person_id FROM nurse;")
    nurses_id = cur.fetchall()

    for chart in charts:
        for i in range(10):
            chart_id, chart_start_date = chart[0], chart[1]

            cr_time = fake.date_time_between(start_date=chart_start_date, end_date="now", tzinfo=None)

            res_cons = fake.paragraph(nb_sentences=fake.random_int(min=1, max=3, step=1), variable_nb_sentences=True, ext_word_list=None)

            doctor_id = random.choice(doctors_id)[0]

            nurse_id = random.choice(nurses_id)[0]

            query = "insert into report(create_time, results_of_consultation, chart_id, doctor_id, nurse_id) " \
                    "values (%s, %s, %s, %s, %s);"

            cur.execute(query, (cr_time, res_cons, chart_id, doctor_id, nurse_id))
            query = query % (cr_time, res_cons, chart_id, doctor_id, nurse_id)
            write_into_file(query)


def inserting_nurse_qual():
    cur.execute("select person_id from nurse;")
    nurses = cur.fetchall()
    quals = ['qual1', 'qual2', 'qual3']
    for nurse in nurses:
        fake_quals = quals.copy()
        # print(nurse[0], fake_quals)
        for i in range(1, fake.random_int(min=1, max=3, step=1)):
            qual = fake.word(ext_word_list=fake_quals)
            fake_quals.remove(qual)
            query = "insert into nurse_qualifications(descrip, person_id) values (%s, %s);"
            cur.execute(query, (qual, nurse[0]))
            query = query % (qual, nurse[0])
            write_into_file(query)


def inserting_doctor_qual():
    cur.execute("select person_id from doctor;")
    docs = cur.fetchall()
    quals = ['qual1', 'qual2', 'qual3']
    for doc in docs:
        fake_quals = quals.copy()
        # print(nurse[0], fake_quals)
        for i in range(1, fake.random_int(min=1, max=3, step=1)):
            qual = fake.word(ext_word_list=fake_quals)
            fake_quals.remove(qual)
            query = "insert into doctor_qualifications(descrip, person_id) values (%s, %s);"
            cur.execute(query, (qual, doc[0]))
            query = query % (qual, doc[0])
            write_into_file(query)


def inserting_nurse_assigned():
    cur.execute("select person_id from doctor;")
    doctors = cur.fetchall()
    for doc in doctors:
        doc_id = doc[0]
        cur.execute("select person_id from nurse order by random() limit 1;")
        nurse_id = cur.fetchone()[0]
        query = "insert into nurse_assigned(doc_id, nurse_id) values (%s, %s);"
        cur.execute(query, (doc_id, nurse_id))
        query = query % (doc_id, nurse_id)
        write_into_file(query)


def inserting_req_med():
    cur.execute("SELECT person_id FROM doctor;")
    doctors_id = cur.fetchall()

    cur.execute("SELECT person_id FROM nurse;")
    nurses_id = cur.fetchall()

    cur.execute("SELECT medicine_id FROM medicine;")
    meds = cur.fetchall()

    for i in range(50):
        doctor_id = random.choice(doctors_id)[0]
        nurse_id = random.choice(nurses_id)[0]
        med_id = random.choice(meds)[0]

        query = "insert into request_medicine(doctor_id, nurse_id, medicine_id) VALUES (%s, %s, %s)"
        cur.execute(query, (doctor_id, nurse_id, med_id))
        query = query % (doctor_id, nurse_id, med_id)
        write_into_file(query)


def inserting_provide_serv():
    cur.execute("SELECT person_id FROM doctor;")
    doctors_id = cur.fetchall()

    cur.execute("SELECT person_id FROM nurse;")
    nurses_id = cur.fetchall()

    cur.execute("SELECT service_id FROM service;")
    sers = cur.fetchall()

    for i in range(50):
        doctor_id = random.choice(doctors_id)[0]
        nurse_id = random.choice(nurses_id)[0]
        ser_id = random.choice(sers)[0]

        query = "insert into provide_service(doctor_id, nurse_id, ser_id) VALUES (%s, %s, %s)"
        cur.execute(query, (doctor_id, nurse_id, ser_id))
        query = query % (doctor_id, nurse_id, ser_id)
        write_into_file(query)


def inserting_order():
    cur.execute("SELECT person_id FROM doctor;")
    doctors = cur.fetchall()
    for i in range(50):
        doctor_id = random.choice(doctor_id)[0]
        query_order = "INSERT INTO \"order\"(doc_id) VALUES (%s);"
        cur.execute(query_order % doctor_id)
        query_order = query_order % doctor_id
        write_into_file(query_order)


def inserting_order_ser():
    cur.execute("select order_id from \"order\";")
    orders = cur.fetchall()

    cur.execute('select service_id from service;')
    sers = cur.fetchall()
    for order in orders:
        order_id = order[0]
        service_id = random.choice(sers)[0]
        query_order_serv = "insert into order_service(order_id, service) VALUES (%s, %s);"
        cur.execute(query_order_serv, (order_id, service_id))
        query_order_serv = query_order_serv % (order_id, service_id)
        write_into_file(query_order_serv)


def inserting_order_med():
    cur.execute("select order_id from \"order\";")
    orders = cur.fetchall()

    cur.execute('select medicine_id from medicine;')
    meds = cur.fetchall()

    for order in orders:
        order_id = order[0]
        med_id = random.choice(meds)[0]
        query_order_serv = "insert into order_medicine(order_id, medicine) VALUES (%s, %s);"
        cur.execute(query_order_serv, (order_id, med_id))
        query_order_serv = query_order_serv % (order_id, med_id)
        write_into_file(query_order_serv)


def inserting_invoices():
    cur.execute("select person_id from patient;")
    patients_id = cur.fetchall()
    cur.execute("select order_id from \"order\";")
    orders_id = cur.fetchall()
    for patient in patients_id:
        for i in range(1, fake.random_int(min=1, max=3, step=1)):
            patient_id = patient[0]
            invoice_date = fake.date_between(start_date="-10y", end_date="today")
            payment_due = fake.date_between(start_date=invoice_date, end_date="today")
            tax_amount = fake.random_int(min=1, max=30, step=1)
            order_id = random.choice(orders_id)[0]
            cur.execute("select order_medicine.medicine "
                        "from \"order\", order_medicine where order_medicine.order_id = %s;" % order_id)
            medicine_id = cur.fetchone()[0]
            cur.execute("select price from medicine where medicine_id = %s" % medicine_id)
            price_med = cur.fetchone()[0]

            cur.execute("select order_service.service "
                        "from \"order\", order_service where order_service.order_id = %s;" % order_id)
            service_id = cur.fetchone()[0]
            cur.execute("select price from service where service.service_id = %s" % service_id)
            price_ser = cur.fetchone()[0]
            total = price_med + price_ser
            query = "insert into invoice(patient_id, invoice_date, payment_due_date, tax_amount, total_amount, inv_id) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(query, (patient_id, invoice_date, payment_due, tax_amount, total, order_id))
            query = query % (patient_id, invoice_date, payment_due, tax_amount, total, order_id)
            write_into_file(query)


def inserting_manage_invoices():
    print("Start manage_invoice")
    cur.execute("select person_id from accountant;")
    accountants = cur.fetchall()

    cur.execute("select inv_id from invoice;")
    invoices = cur.fetchall()

    for invoice in invoices:
        invoice_id = invoice[0]
        accountant_id = random.choice(accountants)[0]
        query = "insert into manage_invoice(acc_id, inv_id) values (%s, %s);"
        cur.execute(query, (accountant_id, invoice_id))
        query = query % (accountant_id, invoice_id)
        write_into_file(query)


def inserting_complete_order():
    cur.execute("select order_id from \"order\";")
    orders = cur.fetchall()

    cur.execute("select person_id from storekeeper;")
    stks = cur.fetchall()

    for order in orders:
        order_id = order[0]
        stk_id = random.choice(stks)[0]
        query = "insert into complete_order(order_id, stk_id) values (%s, %s);"
        cur.execute(query, (order_id, stk_id))
        query = query % (order_id, stk_id)
        write_into_file(query)


# cur.execute("delete from complete_order;")
# cur.execute("delete from manage_invoice;")
# cur.execute("delete from invoice;")
# cur.execute("delete from order_medicine;")
# cur.execute("delete from order_service;")
# cur.execute("delete from order;")
# cur.execute("delete from provide_service;")
# cur.execute("delete from service;")
# cur.execute("delete from request_medicine;")
# cur.execute("delete from nurse_assigned;")
# cur.execute("DELETE FROM nurse_qualifications;")
# cur.execute("DELETE FROM doctor_qualifications;")
# cur.execute("DELETE FROM report;")
# cur.execute("DELETE FROM medical_chart;")
# cur.execute("DELETE FROM patient;")
# cur.execute("DELETE FROM doctor;")
# cur.execute("DELETE FROM nurse;")
# cur.execute("DELETE FROM accountant;")
# cur.execute("DELETE FROM receptionist;")
# cur.execute("DELETE FROM storekeeper;")
# cur.execute("DELETE FROM person")
# cur.execute("DELETE FROM appointment")
# inserting_patients()
# inserting_doctors()
# inserting_nurses()
# inserting_accountants()
# inserting_receptionists()
# inserting_storekeepers()
# inserting_medicines()
# inserting_services()
# inserting_appointments()
# inserting_medical_charts()
# inserting_reports()
# inserting_nurse_qual()
# inserting_doctor_qual()
# inserting_nurse_assigned()
# inserting_req_med()
# inserting_provide_serv()
# inserting_order()
# inserting_order_ser()
# inserting_order_med()
# inserting_invoices()
# inserting_manage_invoices()
# inserting_complete_order()

# Make the changes to the database persistent
con.commit()

# Close communication with the database
cur.close()
con.close()

# close file
file_output.close()
