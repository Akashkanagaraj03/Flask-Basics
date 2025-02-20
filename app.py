from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import sql

DB_HOST = 'localhost'
DB_NAME = 'flask'
DB_USER = 'postgres'
DB_PASSWORD = '1243'

app = Flask(__name__)
@app.route('/get-students', methods=['GET'])
def get_students():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students;")

        students = cursor.fetchall()

        if not students:
            return jsonify({"message": "No users found"}), 404

        students_list = []
        for student in students:
            students_list.append({
                "id": student[1],
                "name": student[1],
                "email": student[2]
            })
        cursor.close()
        connection.close()

        return jsonify(students_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
