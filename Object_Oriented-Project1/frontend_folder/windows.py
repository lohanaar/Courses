#Import Modules
import sqlite3
from backend_folder.summary import GlucoseSummary
from backend_folder.insulin_intake import InsulinApp
from backend_folder.alarm import Alarm, datetime
import tkinter as tk
from tkinter import messagebox

#Class to handle glucose and carbohydrate entry
class NewEntryWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Insert Glucose/Carbohydrates')
        self.geometry("300x200")

        # Create an instance for the InslulinApp class
        self.insulin_app = InsulinApp()

        # Glucose and Carbs entry fields
        tk.Label(self, text='Glucose(mmol/L):').pack(pady=5)
        self.entry_glucose = tk.Entry(self)
        self.entry_glucose.pack(pady=5)

        tk.Label(self, text='Carbohydrates(g):').pack(pady=5)
        self.entry_carbs = tk.Entry(self)
        self.entry_carbs.pack(pady=5)

        tk.Button(self, text='Save and Calculate Insulin', command=self.insulin_count).pack(pady=10)


    #Calculate insulin based on glucose and carbs input
    def insulin_count(self):

        try:
            glucose = float(self.entry_glucose.get())
            carbs = float(self.entry_carbs.get())

            self.destroy()  # close the NewEntryWindow

            #Check if the input values are positive
            if glucose < 0 or carbs < 0:
                messagebox.showerror('ERROR!', 'Only positive numbers are accepted!')

            else:
                insulin = self.insulin_app.insulin_count(glucose, carbs)

                #Saving the data
                self.insulin_app.add_values(glucose, carbs, insulin)

                #Show insulin dosage
                messagebox.showinfo('Your datas are save!!!', f'Insulin needed: {insulin} units')

        except ValueError:
            messagebox.showerror('ERROR!', 'Please insert a valid number!')

#Class to handle alarm creation
class AlarmWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Create a New Alarm')
        self.geometry("300x200")

        # Create an instance for the Alarm class
        self.alarm = Alarm()

        tk.Label(self, text="Add Alarm (HH:MM):").pack(pady=5)
        self.entry_alarm = tk.Entry(self)
        self.entry_alarm.pack(pady=5)

        tk.Button(self, text="Create Alarm", command=self.set_alarm).pack(pady=10)

    #Set the alarm based on the user input
    def set_alarm(self):
        try:
            time = self.entry_alarm.get()
            hour, minute = map(int, time.split(':')) #Get hour and minute from the input
            target = self.alarm.convert_datetime(hour, minute) #Convert to datetime object

            #If the input is in the past, a warning message box will pop up
            if target <= datetime.now():
                messagebox.showwarning('ATTENTION!!!','The time you entered has already passed. Please enter a future time for the alarm.')

            else:
                self.alarm.set_alarm(target) #Wait until the time is reached
                messagebox.showinfo('Alarm', f'Time to check your glucose!!!')
                self.destroy()  # close the AlarmWindow

        except ValueError:
            messagebox.showerror('ERROR!', 'Please insert the hour and minutes in a valid format (HH:MM)!')

#Class to generate glucose summary for different periods
class SummaryWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Summary')
        self.geometry("300x200")

        # Create an instance for the GlucoseSummary class
        self.summary = GlucoseSummary()

        tk.Label(self, text="Choose the range:").pack(pady=5)
        self.period_var = tk.IntVar()
        tk.Radiobutton(self, text="3 days", variable=self.period_var, value=3).pack()
        tk.Radiobutton(self, text="7 days", variable=self.period_var, value=7).pack()
        tk.Radiobutton(self, text="15 days", variable=self.period_var, value=15).pack()

        tk.Button(self, text="Create Summary", command=self.generate_summary).pack(pady=10)


    #Generate summary based on the choose range period
    def generate_summary(self):
        try:
            days_range = int(self.period_var.get()) # Get the selected period
            self.summary.create_view(days_range)
            avg_glucose = self.summary.avg_glucose()
            high_perc, in_range_perc, low_perc = self.summary.range_glucose()
            self.summary.drop_view() #drop the view after use

            self.destroy() #close the SummaryWindow

            #Display the summary in a message box
            messagebox.showinfo(f'Summary of the last {days_range} days',
            f"""
            ________________________________
            
                Avg Glucose: {avg_glucose}mmol/L
            ________________________________ 
                                       
                    Time in Range
            
             High: {high_perc}%
             In Range: {in_range_perc}%
             Low: {low_perc}%
            ________________________________
            """
            )
        except sqlite3.OperationalError:
            messagebox.showerror('ERROR!', 'There is no data available! You must insert glucose/carbs first.')

#Class to show user guide
class UserGuideWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('User Guide')
        self.geometry('700x400')

        #Adding the text with the app's instructions
        text= ("""
                                    User Guide
_______________________________________________________________________________
        
                Welcome to the Diabetes App! Below, you will find
               instructions on how to use the app's main features.
_______________________________________________________________________________
        
                                    Main Page
                
            The main page contains three primary buttons for navigation:
-------------------------------------------------------------------------------

 1. Insert Glucose/Carbs
    - In this option, you can input your blood glucose level and the amount 
      of carbohydrates consumed at the current time.
    - Once submitted, the app will save the values and calculate the required 
      insulin dose you need to take.
    
 Notes:
    - Negative or blank values are not allowed.
    - If you wish to input only one of the values (glucose or carbs), the other
      must be set to 0.
-------------------------------------------------------------------------------
 2. Generate Summary
    - This feature allows you to view a summary of your blood glucose levels 
      over the past:
        - 3 days
        - 7 days
        - 15 days
    
    - The summary includes:
    
    1. The average glucose level during the selected period.
    
    2. The percentage of time your glucose fell into the following ranges:
        - Low: Glucose values equal to or below 4 mmol/L.
        - In Range: Ideal glucose values — greater than 4 mmol/L but less than
          or equal to 10 mmol/L.
        - High: Glucose values greater than 10 mmol/L.
        
 Note: If you are a new user with no previously saved glucose data, you will not
 be able to use this feature.
-------------------------------------------------------------------------------
 3. New Alarm
    - Use this option to set a time for your next alarm for the current day.
    - This feature is particularly helpful to remind you to check your glucose
      levels at specific times.
    
 Note: When the alarm rings, a new window will appear as a notification.
_______________________________________________________________________________
 
 General Note:
    - Ensure all values are entered accurately to receive reliable insulin 
      recommendations and summaries.
        """)

        #Text widget with scrollbar to display the text
        guide_frame= tk.Frame(self)
        guide_frame.pack(fill='both', expand=True)

        # Text widget to display the guide text
        text_widget = tk.Text(guide_frame, wrap="word", padx=10, pady=10)
        text_widget.insert("1.0", text)  # Insert guide text
        text_widget.config(state="disabled")  # Make it read-only
        text_widget.pack(side="left", expand=True)

        # Scrollbar widget
        scrollbar = tk.Scrollbar(guide_frame, command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the Text widget
        text_widget.config(yscrollcommand=scrollbar.set)

