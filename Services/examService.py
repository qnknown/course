import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Services.validation import Validation

class Exams:
    def __init__(self, connection):
        self.connection = connection

    @Validation.access_control
    def save_data(self, name, subject1, subject2, subject3, creative):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO exams (name, subject1, subject2, subject3, creative)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, subject1, subject2, subject3, creative))

            self.connection.commit()  # Зберігаємо зміни в базі даних
            QtWidgets.QMessageBox.information(None, "Успіх", "Дані успішно відправлені!")

        except pymysql.MySQLError as e:
            print(f"Помилка збереження даних: {e}")

    @Validation.access_control
    def delete_selected_record(self, table_widget):
        selected_row = table_widget.currentRow()

        if selected_row == -1:
            print("Не вибрано жодного запису для видалення.")
            return

        record_id = table_widget.item(selected_row, 0).text()

        try:
            with self.connection.cursor() as cursor:
                sql_query = "DELETE FROM exams WHERE id = %s"
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
                    sql_query = "SELECT id, name, subject1, subject2, subject3, creative FROM exams"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(6)

                column_headers = ["ID", "Назва", "Предмет 1", "Предмет 2", "Предмет 3", "Творчий"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, name, subject1, subject2, subject3, creative 
            FROM exams 
            WHERE name LIKE '%{keyword}%'
            """
        else:
            query = None

        self.load_data_to_tablewidget(table_widget, query)

    @Validation.access_control
    def update_data(self, table_widget):
        try:
            with self.connection.cursor() as cursor:
                row_count = table_widget.rowCount()
                for row in range(row_count):
                    id_item = table_widget.item(row, 0)
                    name_item = table_widget.item(row, 1)
                    subject1_item = table_widget.item(row, 2)
                    subject2_item = table_widget.item(row, 3)
                    subject3_item = table_widget.item(row, 4)
                    creative_item = table_widget.item(row, 5)

                    # Debug prints
                    print(f"Row {row}:")
                    print(f"ID: {id_item.text() if id_item else 'None'}")
                    print(f"Name: {name_item.text() if name_item else 'None'}")
                    print(f"Subject 1: {subject1_item.text() if subject1_item else 'None'}")
                    print(f"Subject 2: {subject2_item.text() if subject2_item else 'None'}")
                    print(f"Subject 3: {subject3_item.text() if subject3_item else 'None'}")
                    print(f"Creative: {creative_item.text() if creative_item else 'None'}")

                    if all([id_item, name_item, subject1_item, subject2_item, subject3_item, creative_item]):
                        try:
                            id = int(id_item.text())
                            name = name_item.text()
                            subject1 = subject1_item.text()
                            subject2 = subject2_item.text()
                            subject3 = subject3_item.text()
                            creative = int(creative_item.text())

                            update_query = """
                                UPDATE exams
                                SET name = %s, subject1 = %s, subject2 = %s, subject3 = %s, creative = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (name, subject1, subject2, subject3, creative, id))
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

    def load_combobox_data(self, comboBox_subject1, comboBox_subject2, comboBox_subject3, comboBox_creative):
        try:
            with self.connection.cursor() as cursor:
                # Load subjects into the comboboxes
                cursor.execute("SELECT subjectID, name FROM subjects")
                subjects = cursor.fetchall()

                comboBox_subject1.clear()
                comboBox_subject2.clear()
                comboBox_subject3.clear()

                for subject in subjects:
                    comboBox_subject1.addItem(subject[1], subject[0])
                    comboBox_subject2.addItem(subject[1], subject[0])
                    comboBox_subject3.addItem(subject[1], subject[0])

                # Load the creative exam status into combobox
                comboBox_creative.clear()
                comboBox_creative.addItem("Ні", 0)
                comboBox_creative.addItem("Так", 1)

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")
