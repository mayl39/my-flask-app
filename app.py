from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ตั้งค่าการเชื่อมต่อกับฐานข้อมูล MySQL บน Azure
def get_db_connection():
    connection = mysql.connector.connect(
        host='your_mysql_server.mysql.database.azure.com',
        user='your_username@your_mysql_server',
        password='your_password',
        database='your_database_name',
        ssl_ca='path_to_certificate.pem'  # ถ้าจำเป็น
    )
    return connection

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM your_table_name')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
