import psycopg2


class sql_connection:
    connection = None

    def connect_db(self, user, password, database):
        try:
            self.connection = psycopg2.connect(user=user,
                                               password=password,
                                               host="localhost",
                                               # host="127.0.0.1",
                                               port="5432",
                                               database=database)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def insert_data_row(self, table_name, field_names, values):
        cursor = self.connection.cursor()

        line_to_write = "INSERT INTO " + table_name + " ("

        if len(field_names) == 1:
            line_to_write += field_names[0] + ") VALUES ('" + values[0] + "')"
        else:
            for i in range(0, len(field_names) - 1):
                line_to_write += field_names[i]
                line_to_write += ", "
            line_to_write += field_names[len(field_names) - 1]
            line_to_write += ") VALUES ("

            for i in range(0, len(values) - 1):
                line_to_write += "'" + values[i] + "'"
                line_to_write += ", "
            line_to_write += "'" + values[len(values) - 1] + "'"
            line_to_write += ")"

        print(line_to_write)
        cursor.execute(line_to_write)

        self.connection.commit()
        cursor.close()
