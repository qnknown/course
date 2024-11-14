import pymysql
from PyQt5.QtWidgets import QMessageBox
import globals

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

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = "SELECT * FROM `keys` WHERE username=%s AND password=%s"
            cursor.execute(query, (username.strip(), password.strip()))
            result = cursor.fetchone()

            # Дебаг
            print(f"Query executed: {query}")
            print(f"Username: {username.strip()}, Password: {password.strip()}")
            print(f"Result: {result}")

            if result:
                if 'access' in result:
                    globals.user_access = result['access']
                    print(f"User access level: {globals.user_access}")
                    return True
                else:
                    print("Access field not found in the result.")
                    return False
            else:
                print("Invalid username or password.")
                return False

    except pymysql.MySQLError as e:
        print(f"MySQL error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
