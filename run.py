import connect_to_db
from generate_data import GenerateData

pol = connect_to_db.sql_connection()

fields = ["id", "imie", "nazw"]
values = ["12", "michal", "duk"]

gd = GenerateData()
test_emp = gd.generate_employee()
test_data = gd.generate_procedure()
test_trip = gd.generate_trip()

pol.connect_db("postgres", "admin", "postgres")
print(test_trip[0])
print(test_trip[1])
pol.insert_data_row('employee', test_emp[0], test_emp[1])


