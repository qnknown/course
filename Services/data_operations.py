import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

def save_data(connection, name, specialty_id, is_privileged, transfer):
    if connection is None:
        print("З'єднання з базою даних не встановлене.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM applicants WHERE name = %s", (name,))
            existing_application = cursor.fetchone()

            if existing_application:
                print("Ви вже подали заяву на одну спеціальність.")
                QtWidgets.QMessageBox.warning(None, "Помилка", "Ви вже подали заяву на одну спеціальність.")
                return

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

        connection.commit()
        QtWidgets.QMessageBox.information(None, "Успіх", "Заява успішно подана!")

    except pymysql.MySQLError as e:
        print(f"Помилка збереження даних: {e}")
