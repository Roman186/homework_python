from sqlalchemy import create_engine, inspect, text


class SubjectTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        names_tables = inspector.get_table_names()

        return names_tables

    def select_one_filters(self, subj_id):
        connection = self.db.connect()
        sql_statement = text(
            "SELECT subject_title FROM subject \
             WHERE subject_id = :id_subj")
        result = connection.execute(
            sql_statement, {"id_subj": f"{subj_id}"})
        rows = result.mappings().all()

        return rows

    def get_max_subject_id(self):
        connection = self.db.connect()
        result = connection.execute(
            text("SELECT MAX(subject_id) FROM subject"))
        max_id = result.scalar() or 0
        connection.close()
        return max_id

    def insert_in_table(self, subject_id, subject):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(
            "INSERT INTO subject(subject_id, subject_title) \
             VALUES (:new_id, :new_subject)")
        connection.execute(sql, {"new_id": f"{subject_id}",
                                 "new_subject": f"{subject}"})

        transaction.commit()
        connection.close()

    def update_subject(self, subject_id, new_title):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text(
            "UPDATE subject SET subject_title = :subj_title \
             WHERE subject_id = :id")
        connection.execute(
            sql, {"subj_title": new_title,
                  "id": subject_id})

        transaction.commit()
        connection.close()

    def delete_subject(self, id_num):
        connection = self.db.connect()
        transaction = connection.begin()

        sql = text("DELETE FROM subject WHERE subject_id = :id_subj")
        connection.execute(sql, {"id_subj": f"{id_num}"})

        transaction.commit()
        connection.close()
