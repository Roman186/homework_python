from sqlalchemy import create_engine, inspect, text
import psycopg2


class CustomersTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        names_tables = inspector.get_table_names()

        return names_tables

    def select_from_table(self):
        connection = self.db.connect()
        result = connection.execute(text("SELECT * FROM customers"))
        rows = result.mappings().all()

        connection.close()

        return rows

    def select_one_filters(self, id_custom):
        connection = self.db.connect()
        sql_statement = text(
            "SELECT customer_nm FROM customers \
             WHERE customer_id = :id_customer")
        result = connection.execute(
            sql_statement, {"id_customer": f"{id_custom}"})
        rows = result.mappings().all()

        return rows

    def select_order_by_desc_id(self):
        connection = self.db.connect()
        result = connection.execute(text(
            "SELECT * FROM customers ORDER BY customer_id DESC"))
        rows = result.mappings().all()

        connection.close()

        return rows[0]

    def insert_in_table(self, custom_id, custom_nm):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(
            "INSERT INTO customers(customer_id, customer_nm) \
             VALUES (:new_id, :new_name)")
        connection.execute(sql, {"new_id": f"{custom_id}",
                                 "new_name": f"{custom_nm}"})

        transaction.commit()
        connection.close()

    def update_subject(self):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(
            "UPDATE customers SET customer_nm = :nm_customer \
             WHERE customer_id = :id")
        connection.execute(
            sql, {"nm_customer": "changed customer",
                                 "id": 99999})

        transaction.commit()
        connection.close()

    def delete_subject(self, id_number):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text("DELETE FROM customers WHERE customer_id = :id")
        connection.execute(sql, {"id": f"{id_number}"})

        transaction.commit()
        connection.close()
