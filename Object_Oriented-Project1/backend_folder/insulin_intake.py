# Import Modules
import sqlite3
from datetime import datetime

#Manage the Insulin calculation and data logging
class InsulinApp:
    def __init__(self, filename = 'DiabetesApp.db'):
        self.filename = filename
        #If the file doesn't exist (new user), it will be created
        conn = sqlite3.connect(self.filename)

        #cursor to execute SQL queries
        cur = conn.cursor()

        #Creates a table if it doesn't exist
        cur.execute('''CREATE TABLE IF NOT EXISTS tracker (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            check_date DATE,
            check_time TIME,
            glucose DECIMAL,
            carbs INTEGER,
            insulin INTEGER
        )''')

        conn.commit()
        conn.close()

    #Method that adds glucose, carbs and insulin to the database
    def add_values(self, glucose, carbs, insulin):
        ck_date= datetime.now().strftime('%Y-%m-%d') #Current date
        ck_time = datetime.now().strftime('%H:%M:%S') #Current time

        try:
            conn = sqlite3.connect(self.filename)
            cur = conn.cursor()

            sql_insert = """INSERT INTO tracker (check_date, check_time, glucose, carbs, insulin) VALUES (?, ?, ?, ?, ?)"""
            all_data = (ck_date, ck_time, glucose, carbs, insulin)

            cur.execute(sql_insert, all_data) #Insert data into the db

            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)

    #Calculate the required insulin based on glucose and carbs input
    def insulin_count(self, glucose, carbs):
        var_to_count = {
            'glucose_goal' : 8, #target glucose level
            'drop_unit' : 2, # 1u insulin drops glucose by 2 mmol/L
            'carbs_insulin' : 12, # For each 12g of carbs, 1u of insulin is required
        }
        total_insulin = 0

        #Calculate insulin needed based on glucose
        if glucose > var_to_count['glucose_goal']:
            total_insulin += (glucose - var_to_count['glucose_goal'])/var_to_count['drop_unit']

        #Calculate insulin  based on carbohydrates
        if carbs >= var_to_count['carbs_insulin']:
            total_insulin += carbs/var_to_count['carbs_insulin']

        return round(total_insulin, 0)
