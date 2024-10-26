from PyQt5.QtWidgets import QMessageBox
import pymysql

def reset(lineEdit):
    username = lineEdit.text().strip()

    if not username:
        QMessageBox.warning(None, "Input Error", "Введіть юзернейм.")
        return

    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306,
            database='course'
        )

        with connection.cursor() as cursor:
            # Query to fetch data from the `keys` table for the given username
            cursor.execute("SELECT idkeys, username, password, access FROM `keys` WHERE username = %s", (username,))
            keys_data = cursor.fetchall()

            if not keys_data:
                QMessageBox.information(None, "Нема результатів", "Не знайдено ключів для заданого юзернейму.")
            else:
                # Format the data into a readable string
                keys_info = "\n".join([f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}, Access: {row[3]}" for row in keys_data])

                # Display the data in a QMessageBox
                QMessageBox.information(None, "Keys Data", keys_info)

    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
    finally:
        # Close the connection to the database
        if connection:
            connection.close()
