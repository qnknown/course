import pymysql


def create_user_with_privileges(host, user, password, new_user, new_password):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=3306
        )
        cursor = connection.cursor()

        create_user_query = f"CREATE USER '{new_user}'@'localhost' IDENTIFIED BY '{new_password}'"
        cursor.execute(create_user_query)

        grant_privileges_query = f"GRANT ALL PRIVILEGES ON *.* TO '{new_user}'@'localhost' WITH GRANT OPTION"
        cursor.execute(grant_privileges_query)

        cursor.execute("FLUSH PRIVILEGES")

        print(f"User '{new_user}' created and granted all privileges.")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:

        cursor.close()
        connection.close()


create_user_with_privileges(
    host='localhost',
    user='root',
    password='root',
    new_user='new_user',
    new_password='new'
)
