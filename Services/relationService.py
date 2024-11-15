import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Services.validation import Validation

class Relations:
    def __init__(self, connection):
        self.connection = connection

    @Validation.access_control
    def save_data(self, exam_id, teacher_id):
        if self.connection is None:
            print("Database connection is not established.")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO examteachers (exam_id, teacher_id)
                VALUES (%s, %s)
                """
                cursor.execute(sql, (exam_id, teacher_id))

            self.connection.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data successfully saved!")

        except pymysql.MySQLError as e:
            print(f"Error saving data: {e}")

    @Validation.access_control
    def delete_selected_record(self, table_widget):
        selected_row = table_widget.currentRow()

        if selected_row == -1:
            print("No record selected for deletion.")
            return

        record_id = table_widget.item(selected_row, 0).text()

        try:
            with self.connection.cursor() as cursor:
                sql_query = "DELETE FROM examteachers WHERE id = %s"
                cursor.execute(sql_query, (record_id,))
                self.connection.commit()

                print(f"Record with ID {record_id} was successfully deleted.")

                self.load_data_to_tablewidget(table_widget)

        except pymysql.MySQLError as e:
            print(f"Error deleting record: {e}")

    def load_data_to_tablewidget(self, table_widget, query=None):
        try:
            with self.connection.cursor() as cursor:
                if query is None:
                    sql_query = "SELECT id, exam_id, teacher_id FROM examteachers"
                else:
                    sql_query = query
                cursor.execute(sql_query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(3)

                column_headers = ["ID", "Екзамен ID", "Викладач ID"]
                table_widget.setHorizontalHeaderLabels(column_headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Error loading data to table widget: {e}")

    def search_data(self, keyword, table_widget):
        if keyword:
            query = f"""
            SELECT id, exam_id, teacher_id 
            FROM examteachers 
            WHERE exam_id LIKE '%{keyword}%' OR teacher_id LIKE '%{keyword}%'
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
                    exam_item = table_widget.item(row, 1)
                    teacher_item = table_widget.item(row, 2)

                    if all([id_item, exam_item, teacher_item]):
                        try:
                            id = int(id_item.text())
                            exam_id = int(exam_item.text())
                            teacher_id = int(teacher_item.text())

                            update_query = """
                                UPDATE examteachers
                                SET exam_id = %s, teacher_id = %s
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (exam_id, teacher_id, id))
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

    def load_exam_combobox_data(self, comboBox_exams):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM exams")
                exams = cursor.fetchall()

                comboBox_exams.clear()
                for exam in exams:
                    comboBox_exams.addItem(exam[1], exam[0])

        except pymysql.MySQLError as e:
            print(f"Error fetching exam data: {e}")

    def load_teacher_combobox_data(self, comboBox_teachers):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM teachers")
                teachers = cursor.fetchall()

                comboBox_teachers.clear()
                for teacher in teachers:
                    comboBox_teachers.addItem(teacher[1], teacher[0])

        except pymysql.MySQLError as e:
            print(f"Error fetching teacher data: {e}")
