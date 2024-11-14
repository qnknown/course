import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Services.validation import Validation

class Departments:
    def __init__(self, connection):
        self.connection = connection

    @Validation.access_control
    def save_data(self, name, faculty_id):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO departments (name, faculty_id)
                VALUES (%s, %s)
                """
                cursor.execute(sql, (name, faculty_id))

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
                sql_query = "DELETE FROM departments WHERE id = %s"
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
                    sql_query = "SELECT id, name, faculty_id FROM departments"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(3)

                column_headers = ["ID", "Назва", "Факультет"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, name, faculty_id 
            FROM departments 
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
                    faculty_item = table_widget.item(row, 2)


                    # Debug prints
                    print(f"Row {row}:")
                    print(f"ID: {id_item.text() if id_item else 'None'}")
                    print(f"Name: {name_item.text() if name_item else 'None'}")
                    print(f"Faculty ID: {faculty_item.text() if faculty_item else 'None'}")


                    if all([id_item, name_item, faculty_item]):
                        try:
                            id = int(id_item.text())
                            name = name_item.text()
                            faculty_id = int(faculty_item.text())

                            update_query = """
                                UPDATE departments
                                SET name = %s, faculty_id = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (name, faculty_id, id))
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

    def load_combobox_data(self, comboBox_4):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM faculties")
                faculties = cursor.fetchall()

                comboBox_4.clear()
                for faculty in faculties:
                    comboBox_4.addItem(faculty[1], faculty[0])

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")