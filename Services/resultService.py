import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Result:
    def __init__(self, connection):
        self.connection = connection

    def save_data(self, applicant_id, exam_id, score):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
               # SQL-запит для вставки даних в базу
                sql = """
                INSERT INTO examresults (applicant_id, exam_id, score)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (applicant_id, exam_id, score))

            self.connection.commit()  # Зберігаємо зміни в базі даних
            QtWidgets.QMessageBox.information(None, "Успіх", "Дані успішно відправлені!")

        except pymysql.MySQLError as e:
            print(f"Помилка збереження даних: {e}")

    def delete_selected_record(self, table_widget):
        selected_row = table_widget.currentRow()

        if selected_row == -1:
            print("Не вибрано жодного запису для видалення.")
            return

        record_id = table_widget.item(selected_row, 0).text()

        try:
            with self.connection.cursor() as cursor:
                sql_query = "DELETE FROM examresults WHERE id = %s"
                cursor.execute(sql_query, (record_id,))
                self.connection.commit()

                print(f"Запис з ID {record_id} було успішно видалено.")

                self.load_data_to_tablewidget(table_widget)

        except pymysql.MySQLError as e:
            print(f"Помилка при видаленні запису: {e}")

    def load_data_to_tablewidget(self, table_widget, query=None):
        try:
            with self.connection.cursor() as cursor:
                if query is None:
                    sql_query = "SELECT id, applicant_id, exam_id, score FROM examresults"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(4)

                column_headers = ["ID", "Вступник", "Екзамен", "Оцінка"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, applicant_id, exam_id, score 
            FROM examresults
            WHERE applicant_id LIKE '%{keyword}%'
            OR exam_id LIKE '%{keyword}%'
            """
        else:
            query = None

        self.load_data_to_tablewidget(table_widget, query)

    def update_data(self, table_widget):
        try:
            with self.connection.cursor() as cursor:
                row_count = table_widget.rowCount()
                for row in range(row_count):
                    id_item = table_widget.item(row, 0)
                    applicant_id_item = table_widget.item(row, 1)
                    exam_id_item = table_widget.item(row, 2)
                    score_item = table_widget.item(row, 3)

                    # Debug prints
                    print(f"Row {row}:")
                    print(f"ID: {id_item.text() if id_item else 'None'}")
                    print(f"Applicant: {applicant_id_item.text() if applicant_id_item else 'None'}")
                    print(f"Exam: {exam_id_item.text() if exam_id_item else 'None'}")
                    print(f"Score: {score_item.text() if score_item else 'None'}")

                    if all([id_item, applicant_id_item, exam_id_item, score_item]):
                        try:
                            id = int(id_item.text())
                            applicant_id = int(applicant_id_item.text())
                            exam_id = int(exam_id_item.text())
                            score = float(score_item.text())  # Convert to float for DECIMAL type

                            update_query = """
                                UPDATE examresults
                                SET applicant_id = %s, exam_id = %s, score = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (applicant_id, exam_id, score, id))
                        except ValueError as ve:
                            print(f"ValueError in row {row}: {ve}")
                        except Exception as ex:
                            print(f"Exception in row {row}: {ex}")
                    else:
                        print(f"Skipping row {row} due to missing data.")

                self.connection.commit()
                print("Data updated successfully.")

        except pymysql.MySQLError as e:
            print(f"Error updating data: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def load_combobox_data(self, comboBox_8, comboBox_4):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM applicants")
                applicants = cursor.fetchall()

                comboBox_8.clear()
                for applicant in applicants:
                    comboBox_8.addItem(applicant[1], applicant[0])




        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM exams")
                exams = cursor.fetchall()

                comboBox_4.clear()
                for exam in exams:
                    comboBox_4.addItem(exam[1], exam[0])

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")