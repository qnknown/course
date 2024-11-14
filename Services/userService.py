import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import globals

class Users:
    def __init__(self, connection):
        self.connection = connection

    def save_data(self, username, password, access):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = """
                                INSERT INTO `keys` (username, password, access)
                                VALUES (%s, %s, %s)
                                """
                cursor.execute(sql, (username, password, access))

            self.connection.commit()
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
                sql_query = "DELETE FROM `keys` WHERE idkeys = %s"
                cursor.execute(sql_query, (record_id,))
                self.connection.commit()

                print(f"Запис з ID {record_id} було успішно видалено.")

                self.load_data_to_tablewidget(table_widget)

        except pymysql.MySQLError as e:
            print(f"Помилка при видаленні запису: {e}")

    def load_data_to_tablewidget(self, table_widget, query=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT access FROM `keys` WHERE username = %s", (globals.username,))
                access_level = cursor.fetchone()

                if access_level and access_level[0] == "Admin":
                    table_widget.setRowCount(1)
                    table_widget.setColumnCount(1)
                    table_widget.setHorizontalHeaderLabels(["Message"])
                    table_widget.setItem(0, 0, QTableWidgetItem("Access Denied"))
                    return

                if query is None:
                    sql_query = "SELECT idkeys, username, password, access FROM `keys`"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(4)

                column_headers = ["ID", "User", "Pass", "Access"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT idkeys, username, password, access
            FROM `keys` 
            WHERE username LIKE '%{keyword}%'
            """
        else:
            query = None

        self.load_data_to_tablewidget(table_widget, query)


    def update_data(self, username, new_password, new_access):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT access FROM `keys` WHERE username = %s", (globals.username,))
                access_level = cursor.fetchone()

                if access_level and access_level[0] == "Admin":
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setWindowTitle("Access Denied")
                    msg_box.setText("You do not have permission to update data.")
                    msg_box.exec_()
                    return

                update_query = """
                    UPDATE `keys`
                    SET password = %s, access = %s
                    WHERE username = %s
                """
                cursor.execute(update_query, (new_password, new_access, username))
                self.connection.commit()

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Success")
                msg_box.setText(f"Data for user '{username}' updated successfully.")
                msg_box.exec_()

        except pymysql.MySQLError as e:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(f"Error while updating data: {e}")
            msg_box.exec_()


        except pymysql.MySQLError as e:
            print(f"Error updating data for user '{username}': {e}")
        except Exception as e:
            print(f"Unexpected error while updating data for user '{username}': {e}")

    def load_combobox_data(self, comboBox_8, comboBox_4, comboBox_9):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT idkeys, username FROM `keys`")
                users = cursor.fetchall()

                comboBox_8.clear()
                for user in users:
                    comboBox_8.addItem(user[1], user[0])

                comboBox_4.clear()
                comboBox_4.addItems(["Admin", "Operator", "Common"])

                comboBox_9.clear()
                comboBox_9.addItems(["Admin", "Operator", "Common"])

        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")