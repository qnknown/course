import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Services.validation import Validation


class Specialties:
    def __init__(self, connection):
        self.connection = connection

    @Validation.access_control
    def save_data(self, name, department_id, group_id):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO specialties (name, department_id, group_id)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (name, department_id, group_id))

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
                sql_query = "DELETE FROM specialties WHERE id = %s"
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
                    sql_query = "SELECT id, name, department_id, group_id FROM specialties"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(4)

                column_headers = ["ID", "Назва", "Кафедра", "Група"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, name, department_id, group_id
            FROM specialties
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
                    department_item = table_widget.item(row, 2)
                    group_item = table_widget.item(row, 3)

                    if all([id_item, name_item, department_item, group_item]):
                        try:
                            id = int(id_item.text())
                            name = name_item.text()
                            department_id = int(department_item.text())
                            group_id = int(group_item.text())

                            update_query = """
                                UPDATE specialties
                                SET name = %s, department_id = %s, group_id = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (name, department_id, group_id, id))
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

    def load_combobox_data(self, comboBox_department, comboBox_group):
        try:
            # Load departments data
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM departments")
                departments = cursor.fetchall()

                comboBox_department.clear()
                for department in departments:
                    comboBox_department.addItem(department[1], department[0])

            # Load groups data
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT group_id, name FROM grupy")
                groups = cursor.fetchall()

                comboBox_group.clear()
                for group in groups:
                    comboBox_group.addItem(group[1], group[0])

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")
