import pymysql
from PyQt5.QtWidgets import QTableWidgetItem


class Query:
    def __init__(self, connection):
        self.connection = connection

    def display_query_result(self, table_widget, query, headers):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

                table_widget.setRowCount(len(result))
                table_widget.setColumnCount(len(headers))
                table_widget.setHorizontalHeaderLabels(headers)

                for row_index, row_data in enumerate(result):
                    for column_index, cell_data in enumerate(row_data):
                        table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        except pymysql.MySQLError as e:
            print(f"Database error: {e}")

    def query1(self, table_widget):
        query = """
        SELECT grupy.*
        FROM grupy
        JOIN exams ON grupy.exam_id = exams.id
        WHERE exams.subject1 IS NOT NULL
        AND exams.subject2 IS NOT NULL
        AND exams.subject3 IS NOT NULL
        AND exams.creative IS NULL;
        """
        headers = ["ID", "Група", "Екзамен"]
        self.display_query_result(table_widget, query, headers)

    def query12(self, table_widget):
        query = """
        SELECT grupy.*
        FROM grupy
        JOIN exams ON grupy.exam_id = exams.id
        WHERE exams.subject1 IS NOT NULL
        AND exams.subject2 IS NOT NULL
        AND exams.subject3 IS NOT NULL
        AND exams.creative IS NOT NULL;
        """
        headers = ["ID", "Група", "Екзамен"]
        self.display_query_result(table_widget, query, headers)

    def query13(self, table_widget):
        query = """
        SELECT grupy.*
        FROM grupy
        JOIN exams ON grupy.exam_id = exams.id
        WHERE exams.creative = 1;
        """
        headers = ["ID", "Група", "Екзамен"]
        self.display_query_result(table_widget, query, headers)

    def query2(self, table_widget):
        query = """
        SELECT DISTINCT grupy.*
        FROM grupy
        JOIN specialties ON grupy.group_id = specialties.group_id
        GROUP BY grupy.group_id
        HAVING COUNT(DISTINCT specialties.id) > 1;
        """
        headers = ["ID", "Група", "Екзамен"]
        self.display_query_result(table_widget, query, headers)

    def query3(self, table_widget, specialty_id):
        query = f"""
        
        """
        headers = ["Discipline"]
        self.display_query_result(table_widget, query, headers)

    def query4(self, table_widget, specialty_id):
        query = f"""
        
        """
        headers = ["Exam", "Average Score"]
        self.display_query_result(table_widget, query, headers)

    def query5(self, table_widget):
        query = """
        SELECT faculties.name AS faculty_name, COUNT(applicants.id) AS total_applications
        FROM faculties
        JOIN departments ON faculties.id = departments.faculty_id
        JOIN specialties ON departments.id = specialties.department_id
        JOIN applicants ON applicants.specialty_id = specialties.id
        GROUP BY faculties.id;
        """
        headers = ["Факультет", "К-сть заяв"]
        self.display_query_result(table_widget, query, headers)

    def query51(self, table_widget):
        query = """
        SELECT specialties.name AS specialty_name, COUNT(applicants.id) AS total_applications
        FROM specialties
        JOIN applicants ON applicants.specialty_id = specialties.id
        GROUP BY specialties.id;
        """
        headers = ["Спеціальність", "К-сть заяв"]
        self.display_query_result(table_widget, query, headers)

    def query52(self, table_widget):
        query = """
        SELECT specialties.name AS specialty_name, COUNT(applicants.id) AS total_applications
        FROM specialties
        JOIN applicants ON applicants.specialty_id = specialties.id
        GROUP BY specialties.id
        HAVING total_applications < 10;
        """
        headers = ["Спеціальність", "К-сть заяв"]
        self.display_query_result(table_widget, query, headers)

    def query6(self, table_widget):
        query = """
        
        """
        headers = ["Applicant ID", "Name", "Faculty ID", "Specialty ID", "Privileges"]
        self.display_query_result(table_widget, query, headers)

    def query61(self, table_widget):
        query = """

        """
        headers = ["Applicant ID", "Name", "Faculty ID", "Specialty ID", "Privileges"]
        self.display_query_result(table_widget, query, headers)

    def query62(self, table_widget):
        query = """

        """
        headers = ["Applicant ID", "Name", "Faculty ID", "Specialty ID", "Privileges"]
        self.display_query_result(table_widget, query, headers)

    def query7(self, table_widget):
        query = """
        SELECT COUNT(*) AS transfer_count
        FROM applicants
        WHERE applicants.transfer = 1;
        """
        headers = ["К-сть переводів"]
        self.display_query_result(table_widget, query, headers)

    def query71(self, table_widget):
        query = """
        SELECT COUNT(DISTINCT a1.id) AS matched_transfer_count
        FROM applicants a1
        JOIN specialties s1 ON a1.specialty_id = s1.id
        JOIN grupy g1 ON s1.group_id = g1.group_id
        JOIN exams e1 ON g1.exam_id = e1.id
        JOIN applicants a2 ON a1.id = a2.id AND a2.transfer = 1
        JOIN specialties s2 ON a2.specialty_id = s2.id
        JOIN grupy g2 ON s2.group_id = g2.group_id
        JOIN exams e2 ON g2.exam_id = e2.id
        WHERE e1.subject1 = e2.subject1 AND e1.subject2 = e2.subject2 AND e1.subject3 = e2.subject3;
        """
        headers = ["К-сть переводів"]
        self.display_query_result(table_widget, query, headers)

    def query8(self, table_widget):
        query = """
        
        """
        headers = ["Applicant ID", "Exam", "Score"]
        self.display_query_result(table_widget, query, headers)

    def query81(self, table_widget):
        query = """

        """
        headers = ["Applicant ID", "Exam", "Score"]
        self.display_query_result(table_widget, query, headers)

    def query82(self, table_widget):
        query = """

        """
        headers = ["Applicant ID", "Exam", "Score"]
        self.display_query_result(table_widget, query, headers)

    def query83(self, table_widget):
        query = """

        """
        headers = ["Applicant ID", "Exam", "Score"]
        self.display_query_result(table_widget, query, headers)

    def query9(self, table_widget, exam_name=None):
        query = f"""
        
        """
        headers = ["Teacher ID", "Name", "Activity", "Schedule"]
        self.display_query_result(table_widget, query, headers)

    def query10(self, table_widget):
        query = """
        SELECT specialties.name AS specialty_name, departments.name AS department_name, faculties.name AS faculty_name
        FROM specialties
        JOIN departments ON specialties.department_id = departments.id
        JOIN faculties ON departments.faculty_id = faculties.id
        JOIN grupy ON specialties.group_id = grupy.group_id
        JOIN exams ON grupy.exam_id = exams.id
        JOIN subjects ON subjects.subjectID = exams.subject1 OR subjects.subjectID = exams.subject2 OR subjects.subjectID = exams.subject3
        WHERE subjects.name = 'Математика';
        """
        headers = ["Спеціальність", "Кафедра", "Факультет"]
        self.display_query_result(table_widget, query, headers)
