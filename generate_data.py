import string

import names
import random
from datetime import datetime, timedelta
from string import ascii_uppercase


class GenerateData:
    roles = ['nurse', 'keeper', 'doctor', 'receptionist', 'driver']
    blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    hospitals = open('hospitals.txt').read().split()
    cities = open('cities.txt').read().split()
    streets = open('streets.txt').read().split()
    companies = open('companies.txt').read().split()
    emp_id = 3

    def generate_employee(self):
        id = str(self.emp_id)
        self.emp_id += 1
        f_name = names.get_first_name()
        l_name = names.get_last_name()
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        age = str(random.randint(18, 120))
        role = str(random.choice(self.roles))
        return ['emp_id', 'name', 'surname',
                'city', 'street', 'Street_number',
                'Zip_code', 'age', 'role'], [id, f_name,
                                             l_name,
                                             city,
                                             street,
                                             street_num,
                                             zip_code,
                                             age, role]

    def generate_blood_unit(self):
        values = []
        storage = random.randint(1, 14)
        procedure = random.randint(1, 200)
        amount = random.randint(200, 700)
        values.append([storage, procedure, amount])
        return ['storage', 'procedure', 'amount'], values

    def generate_donor(self):
        f_name = names.get_first_name()
        l_name = names.get_last_name()
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        age = str(random.randint(18, 120))
        pesel = (''.join(random.choice(string.digits) for i in range(11)))
        blood_type = str(random.choice(self.blood_types))
        blood_amount_donated = str(random.randint(0, 50) / 10)
        return ['name', 'surname', 'city', 'street',
                'Street_number', 'Zip_code',
                'age', 'pesel', 'blood_type',
                'blood_amount_donated'], \
               [f_name, l_name, city,
                street, street_num,
                zip_code, age, pesel, blood_type,
                blood_amount_donated]

    def generate_blood_storage(self):
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        return ['name', 'city', 'street',
                'Street_number', 'Zip_code'], \
               [name, city, street, street_num, zip_code]

    def generate_eq_storage(self):
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        return ['city', 'street',
                'Street_number', 'Zip_code'], \
               [city, street, street_num, zip_code]

    def generate_hospital(self):
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        return ['name', 'city', 'street',
                'Street_number', 'Zip_code'], \
               [name, city, street, street_num, zip_code]

    def generate_outpost(self):
        name = random.choice(self.hospitals)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        return ['name', 'city', 'street',
                'Street_number', 'Zip_code'], \
               [name, city, street, street_num, zip_code]

    def generate_partners(self):
        name = random.choice(self.companies)
        type = 'sponsor'
        return ['name', 'type'], [name, type]

    def generate_procedure(self):
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 31), random.randint(0, 24),
                        random.randint(0, 60), random.randint(0, 60))
        date = date.strftime("%x %X")
        return ['date'], [date]

    def generate_vehicle(self):
        plate = ''.join(random.choice(ascii_uppercase) for i in range(12))
        type = random.choice(['Truck', 'Van', 'Bus', 'Car'])
        capacity = random.randint(400, 2000)
        return ['Plate_number', 'Type', 'Capacity'], [plate, type, capacity]

    def generate_med_eq(self):
        type = random.randint(1, 10)
        storage = random.randint(1, 5)
        company = random.choice(['bayer', 'medimax', 'coronoplus', 'your destiny', 'live dont die', 'mad health'])
        amount = random.randint(1, 500)
        return ['Eq_type_ID', 'Eq_storage_ID', 'Company', 'Amount'], [type, storage, company, amount]

    def generate_trip(self):
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 31), random.randint(0, 24),
                        random.randint(0, 60), random.randint(0, 60))
        start_date = date.strftime("%x %X")
        end_date = (date + timedelta(days=random.randint(1, 180))).strftime("%x %X")
        cost = random.randint(50, 100000)
        city = random.choice(self.cities)
        street = random.choice(self.streets) + ' st.'
        street_num = str(random.randint(1, 1000))
        zip_code = str(random.randint(10000, 100000))
        return ['Start_date', 'Finish_date', 'cost', 'city', 'street', 'Street_number', 'Zip_code'], [start_date,
                                                                                                      end_date, cost,
                                                                                                      city, street,
                                                                                                      street_num,
                                                                                                      zip_code]

    def generate_workshift(self):
        date = datetime(random.randint(1980, 2020), random.randint(1, 12), random.randint(1, 31), random.randint(0, 24),
                        random.randint(0, 60), random.randint(0, 60))
        start_date = date.strftime("%x %X")
        end_date = (date + timedelta(hours=random.randint(2, 16))).strftime("%x %X")
