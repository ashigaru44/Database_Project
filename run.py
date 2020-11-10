import connect_to_db
from generate_data import GenerateData

pol = connect_to_db.sql_connection()

fields = ["id", "imie", "nazw"]
values = ["12", "michal", "duk"]

gd = GenerateData()
# test_emp = gd.generate_employee()
# # test_data = gd.generate_procedure()
# test_trip = gd.generate_trip()

pol.connect_db("postgres", "admin", "final_db_hope")


# print(test_trip[0])
# print(test_trip[1])
# pol.insert_data_row('employee', test_emp[0], test_emp[1])


def generate_records(func, reps=1):
    for i in range(reps):
        res = exec(func)
        print(type(res))
        print(res)
        try:
            pol.insert_data_row(res[0], res[1], res[2])
        except Exception:
            continue


pol.insert_data_row('equipment_type', ["type"], ["strzykawka"])
pol.insert_data_row('equipment_type', ["type"], ["igla"])
pol.insert_data_row('equipment_type', ["type"], ["lopata"])
pol.insert_data_row('equipment_type', ["type"], ["wanna"])
pol.insert_data_row('equipment_type', ["type"], ["miecz"])

for i in range(1000):
    res = gd.generate_donor()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_outpost()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_employee()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_partners()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_hospital()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_eq_storage()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_blood_storage()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_med_eq()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_procedure()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
for i in range(1000):
    res = gd.generate_trip()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue

for i in range(1000):
    res = gd.generate_vehicle()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue

for i in range(1000):
    res = gd.generate_workshift()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue

for i in range(1000):
    res = gd.generate_order()
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue

for i in range(1000):
    res = gd.generate_blood_unit
    try:
        pol.insert_data_row(res[0], res[1], res[2])
    except Exception:
        continue
