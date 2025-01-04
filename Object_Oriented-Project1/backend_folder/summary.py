#Import Class
import sqlite3

class GlucoseSummary:
    def __init__(self):
        self.conn = sqlite3.connect('DiabetesApp.db') #Connect to db
        self.cur = self.conn.cursor()

    # Create a view for glucose based on the day range
    def create_view (self, day_range: int):
        try:
            self.cur.execute(f"""
            CREATE VIEW IF NOT EXISTS data_range AS
            SELECT id, glucose, check_date
            FROM tracker 
            WHERE check_date > DATE('now', '-{day_range} days') AND check_date <= date('now') """)
            self.conn.commit()
        except FileNotFoundError as e:
            print(f'Error: {e}')

    #verify if the view 'data_range' exists in the db
    def view_exists(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type= 'view' AND name ='data_range'")
        return self.cur.fetchone() is not None #Returns True if view exists or False otherwise

    #Analyzes glucose data and provides percentages for high, in-range, and low glucose levels
    def range_glucose(self):

        if self.view_exists():
            self.cur.execute("""SELECT COUNT(*) AS TOTAL, 
                                COUNT(CASE WHEN glucose > 10 THEN 1 END) AS high,
                                COUNT(CASE WHEN glucose <= 10 AND glucose > 4 THEN 1 END) AS in_range,
                                COUNT(CASE WHEN glucose <= 4 THEN 1 END) AS low
                                FROM data_range
                                """)
            result= self.cur.fetchone()

            total = result[0]
            high = result[1]
            in_range = result[2]
            low = result[3]

            #calculating the percentages for high, in-range, and low glucose
            if total > 0:
                high_perc = round((high/total)*100,2)
                in_range_perc = round((in_range/total)*100,2)
                low_perc = round((low/total)*100,2)
            else:
                high_perc = in_range_perc = low_perc = 0
        else:
            high_perc = in_range_perc = low_perc = 0

        return high_perc, in_range_perc, low_perc

    ## Calculates the average glucose level within the view's data range
    def avg_glucose(self):
        if self.view_exists():
            self.cur.execute("SELECT ROUND(AVG(glucose),2) FROM data_range")
            avg_gluc = self.cur.fetchone()[0]
        else:
            avg_gluc = 0

        return avg_gluc

    #Drop the view from the db
    def drop_view(self):
        self.cur.execute("DROP VIEW IF EXISTS data_range")
        self.conn.commit()