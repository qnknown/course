import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Services.validation import Validation

class Applicants:
    def __init__(self, connection):
        self.connection = connection

    @Validation.access_control
    def save_data(self, name, specialty_id, is_privileged, transfer):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
                # Отримати group_id для вибраної спеціальності
                cursor.execute("SELECT group_id FROM specialties WHERE id = %s", (specialty_id,))
                result = cursor.fetchone()

                if result is None:
                    print("Спеціальність з таким ID не знайдена!")
                    return

                group_id = result[0]

                cursor.execute("SELECT name FROM grupy WHERE group_id = %s", (group_id,))
                group_result = cursor.fetchone()

                if group_result is None:
                    print("Назва групи з таким ID не знайдена!")
                    return

                group_name = group_result[0]

                sql = """
                INSERT INTO applicants (name, specialty_id, is_privileged, transfer, group_name)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, specialty_id, is_privileged, transfer, group_name))

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
                sql_query = "DELETE FROM applicants WHERE id = %s"
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
                    sql_query = "SELECT id, name, specialty_id, is_privileged, transfer, group_name FROM applicants"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(6)

                column_headers = ["ID", "Ім'я", "Спеціальність ID", "Чи є пільги", "Перевод", "Група"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, name, specialty_id, is_privileged, transfer, group_name 
            FROM applicants 
            WHERE name LIKE '%{keyword}%'
            OR group_name LIKE '%{keyword}%'
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
                    specialty_item = table_widget.item(row, 2)
                    is_privileged_item = table_widget.item(row, 3)
                    transfer_item = table_widget.item(row, 4)
                    group_name_item = table_widget.item(row, 5)

                    # Debug prints
                    print(f"Row {row}:")
                    print(f"ID: {id_item.text() if id_item else 'None'}")
                    print(f"Name: {name_item.text() if name_item else 'None'}")
                    print(f"Specialty ID: {specialty_item.text() if specialty_item else 'None'}")
                    print(f"Is Privileged: {is_privileged_item.text() if is_privileged_item else 'None'}")
                    print(f"Transfer: {transfer_item.text() if transfer_item else 'None'}")
                    print(f"Group Name: {group_name_item.text() if group_name_item else 'None'}")

                    if all([id_item, name_item, specialty_item, is_privileged_item, transfer_item, group_name_item]):
                        try:
                            id = int(id_item.text())
                            name = name_item.text()
                            specialty_id = int(specialty_item.text())
                            is_privileged = int(is_privileged_item.text())
                            transfer = int(transfer_item.text())
                            group_name = group_name_item.text()

                            update_query = """
                                UPDATE applicants
                                SET name = %s, specialty_id = %s, is_privileged = %s, transfer = %s, group_name = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (name, specialty_id, is_privileged, transfer, group_name, id))
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

    def load_combobox_data(self, comboBox_8, comboBox_4, comboBox_9):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM specialties")
                specialties = cursor.fetchall()

                comboBox_8.clear()
                for specialty in specialties:
                    comboBox_8.addItem(specialty[1], specialty[0])

                comboBox_4.clear()
                comboBox_4.addItems(["Ні", "Так"])

                comboBox_9.clear()
                comboBox_9.addItems(["Ні", "Так"])

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")