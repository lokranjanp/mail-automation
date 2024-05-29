import mysql.connector
from datetime import datetime
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.cursor = self.conn.cursor()

    def get_birthdays_today(self):
        today = datetime.now().date()
        self.cursor.execute(
            "SELECT name, email, closeness_factor FROM friends WHERE MONTH(birthday) = %s AND DAY(birthday) = %s",
            (today.month, today.day)
        )
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
