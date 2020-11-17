import string
import itertools
import names
import random
from datetime import datetime, timedelta
from string import ascii_uppercase
import connect_to_db

pol = connect_to_db.SqlConnection()
pol.connect_db("postgres", "admin", "db_final")


class GenerateData:
    roles = ['nurse', 'keeper', 'doctor', 'receptionist', 'driver']
    blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    hospitals = open('hospitals.txt').read().split()
    cities = open('cities.txt').read().split()
    streets = open('streets.txt').read().split()
    companies = open('companies.txt').read().split("\n")
    emp_id = 3

    def generate_employee(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        f_name = names.get_first_name()
        l_name = names.get_last_name()
        l_name.lstrip("'")
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        age = str(random.randint(18, 120))
        role = str(random.choice(self.roles))
        return "employee", ['outpost_id', 'name', 'surname',
                            'city', 'street', 'Street_number',
                            'Zip_code', 'age', 'role'], \
               [str(outpost_id), f_name, l_name, city, street,
                street_num, zip_code, age, role]

    def generate_blood_unit(self, bld_strg_ids, proced_ids):
        bld_strg_id = random.randint(1, 100)
        while bld_strg_id in bld_strg_ids:
            bld_strg_id = random.randint(1, 100)
        proced_id = random.randint(1, 100)
        while proced_id in proced_ids:
            proced_id = random.randint(1, 100)
        amount = str(random.randint(200, 700))
        return "blood_unit", ['blood_storage_id', 'procedure_id', 'amount'], \
               [str(bld_strg_id), str(proced_id), amount]

    def generate_donor(self):
        f_name = names.get_first_name()
        l_name = names.get_last_name()
        l_name.lstrip("'")
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        age = str(random.randint(18, 120))
        pesel = (''.join(random.choice(string.digits) for i in range(11)))
        blood_type = str(random.choice(self.blood_types))
        blood_amount_donated = str(random.randint(0, 50) / 10)
        return "donor", ['name', 'surname', 'city', 'street',
                         'Street_number', 'Zip_code',
                         'age', 'pesel', 'blood_type',
                         'blood_amount_donated'], \
               [f_name, l_name, city,
                street, street_num,
                zip_code, age, pesel, blood_type,
                blood_amount_donated]

    def generate_order(self, hospital_ids, outpost_ids):
        hospital_id = random.randint(1, 100)
        while hospital_id in hospital_ids:
            hospital_id = random.randint(1, 100)
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        blood_type = str(random.choice(self.blood_types))
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 28))
        date = date.strftime("%Y-%m-%d")
        priority = 'average'
        return '"Order"', ['hospital_id', 'outpost_id', 'blood_type', 'date', 'priority'], \
               [str(hospital_id), str(outpost_id), blood_type, date, priority]

    def generate_blood_storage(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        return "blood_storage", ['outpost_id', 'name', 'city', 'street',
                                 'Street_number', 'Zip_code'], \
               [str(outpost_id), name, city, street, street_num, zip_code]

    def generate_eq_storage(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        return "equipment_storage", ['outpost_id', 'city', 'street',
                                     'Street_number', 'Zip_code'], \
               [str(outpost_id), city, street, street_num, zip_code]

    def generate_hospital(self):
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        return "hospital", ['name', 'city', 'street',
                            'Street_number', 'Zip_code'], \
               [name, city, street, street_num, zip_code]

    def generate_outpost(self):
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        return "outpost", ['name', 'city', 'street',
                           'Street_number', 'Zip_code'], \
               [name, city, street, street_num, zip_code]

    def generate_partners(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        name = random.choice(self.companies)
        type = 'sponsor'
        return "partner", ['outpost_id', 'name', 'type'], [str(outpost_id), name, type]

    def generate_procedure(self, employee_ids, donors_ids):
        emp_id = random.randint(1, 1000)
        while emp_id in employee_ids:
            emp_id = random.randint(1, 1000)
        donor_id = random.randint(1, 1000)
        while donor_id in donors_ids:
            donor_id = random.randint(1, 1000)
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 28))
        date = date.strftime("%Y-%m-%d")
        return "prodecure", ['emp_id', 'donor_id', 'date'], [str(emp_id), str(donor_id), date]

    def generate_vehicle(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        plate = ''.join(random.choice(ascii_uppercase) for i in range(12))
        type = random.choice(['Truck', 'Van', 'Bus', 'Car'])
        return "vehicle", ['outpost_id', 'plate_number', 'type'], [str(outpost_id), plate, type]

    def generate_med_eq(self, storage_ids, eq_type_ids):
        storage_id = random.randint(1, 100)
        while storage_id in storage_ids:
            storage_id = random.randint(1, 100)
        eq_type_id = 1
        company = random.choice(['bayer', 'medimax', 'coronoplus', 'your destiny', 'live dont die', 'mad health'])
        amount = str(random.randint(1, 500))
        return "medical_equipment", ['eq_storage_id', 'eq_type_id', 'Company', 'Amount'], \
               [str(storage_id), str(eq_type_id), company, amount]

    def generate_trip(self, outpost_ids):
        outpost_id = random.randint(1, 100)
        while outpost_id in outpost_ids:
            outpost_id = random.randint(1, 100)
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 28))
        start_date = date.strftime("%Y-%m-%d")
        end_date = (date + timedelta(days=random.randint(1, 180))).strftime("%Y-%m-%d")
        cost = str(random.randint(50, 100000))
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10, 100)) + '-' + str(random.randint(100, 1000))
        return "trip", ['outpost_id', 'Start_date', 'Finish_date', 'cost', 'city',
                        'street', 'Street_number', 'Zip_code'], \
               [str(outpost_id), start_date, end_date, cost,
                city, street, street_num, zip_code]

    def generate_workshift(self, employee_ids):
        emp_id = random.randint(1, 1000)
        while emp_id in employee_ids:
            emp_id = random.randint(1, 1000)
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 28))
        start_date = date.strftime("%Y-%m-%d")
        end_date = (date + timedelta(hours=random.randint(2, 16))).strftime("%Y-%m-%d")
        return "workshift", ['emp_id', 'start_date', 'finish_date'], [str(emp_id), start_date, end_date]

    def generate_donor_set(self, n):
        for _ in itertools.repeat(None, n):
            res = gd.generate_donor()
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_outpost_set(self, n):
        for _ in itertools.repeat(None, n):
            res = gd.generate_outpost()
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_employee_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_employee(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_partners_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_partners(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_hospital_set(self, n):
        for _ in itertools.repeat(None, n):
            res = gd.generate_hospital()
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_eq_str_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_eq_storage(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_bld_str_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_blood_storage(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_med_eqt_set(self, n):
        storage_ids = pol.check_foreign_key("equipment_storage", "eq_storage_id")
        eq_type_ids = pol.check_foreign_key("equipment_type", "eq_type_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_med_eq(storage_ids, eq_type_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_proced_set(self, n):
        employee_ids = pol.check_foreign_key("employee", "emp_id")
        donors_ids = pol.check_foreign_key("donor", "donor_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_procedure(employee_ids, donors_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_trip_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_trip(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_vehicles_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_vehicle(outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_workshift_set(self, n):
        employee_ids = pol.check_foreign_key("employee", "emp_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_workshift(employee_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_order_set(self, n):
        outpost_ids = pol.check_foreign_key("outpost", "outpost_id")
        hospital_ids = pol.check_foreign_key("hospital", "hospital_id")
        for _ in itertools.repeat(None, n):
            res = gd.generate_order(hospital_ids, outpost_ids)
            pol.insert_data_row(res[0], res[1], res[2])

    def generate_blood_unit_set(self, n):
        bld_strg_ids = pol.check_foreign_key("blood_storage", "blood_storage_id")
        proced_ids = pol.check_foreign_key("prodecure", "procedure_id")
        for u in itertools.repeat(None, n):
            res = gd.generate_blood_unit(bld_strg_ids, proced_ids)
            # try:
            pol.insert_data_row(res[0], res[1], res[2])


gd = GenerateData()

pol.insert_data_row('equipment_type', ["type"], ["strzykawka"])
pol.insert_data_row('equipment_type', ["type"], ["igla"])
pol.insert_data_row('equipment_type', ["type"], ["lopata"])
pol.insert_data_row('equipment_type', ["type"], ["wanna"])
pol.insert_data_row('equipment_type', ["type"], ["miecz"])

gd.generate_donor_set(2000)
gd.generate_outpost_set(100)
gd.generate_employee_set(500)
gd.generate_partners_set(100)
gd.generate_hospital_set(100)
gd.generate_eq_str_set(100)
gd.generate_bld_str_set(100)
gd.generate_med_eqt_set(500)
gd.generate_proced_set(3000)
gd.generate_trip_set(100)
gd.generate_vehicles_set(400)
gd.generate_workshift_set(5000)
gd.generate_order_set(5000)
gd.generate_blood_unit_set(10000)
