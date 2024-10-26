import pymysql
from PyQt5.QtWidgets import QMessageBox


class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            raise Exception("Database connection is not established.")
        return cls._connection

    @classmethod
    def set_connection(cls, connection):
        cls._connection = connection


def login(username, password):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            port=3306,
            database='course'
        )
        DatabaseConnection.set_connection(connection)

        with connection.cursor() as cursor:
            query = "SELECT * FROM `keys` WHERE username=%s AND password=%s"
            cursor.execute(query, (username.strip(), password.strip()))
            result = cursor.fetchone()

            # дебаг
            print(f"Query executed: {query}")
            print(f"Username: {username.strip()}, Password: {password.strip()}")
            print(f"Result: {result}")

            if result:
                return True
            else:
                return False

    except pymysql.MySQLError as e:
        print(f"MySQL error: {e}")
        return False



