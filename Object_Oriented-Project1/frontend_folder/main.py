#Import Modules
import tkinter as tk
from windows import NewEntryWindow, AlarmWindow, SummaryWindow, UserGuideWindow

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        #Main window
        self.title('Diabetes App')
        self.geometry('300x300')

        #Instruction label
        self.label = tk.Label(self, text='Welcome to Diabetes App!!! \n\nPlease choose an option:', font=('Arial', 14))
        self.label.pack(pady=20)

        #Options Buttons
        self.bt_new_entry = tk.Button(self, text='Insert Glucose/Carbs', command= self.open_new_entry_window)
        self.bt_new_entry.pack(pady=10)

        self.bt_summary = tk.Button(self, text='Generate Summary', command= self. open_summary_window)
        self.bt_summary.pack(pady=10)

        self.bt_alarm = tk.Button(self, text='New Alarm', command= self.open_alarm_window)
        self.bt_alarm.pack(pady=10)

        self.bt_help = tk.Button(self, text='Help', command= self.open_user_guide)
        self.bt_help.pack(side='right', anchor='n', padx=20, pady=5)

    def open_new_entry_window(self):
        NewEntryWindow(self)

    def open_alarm_window(self):
        AlarmWindow(self)

    def open_summary_window(self):
        SummaryWindow(self)

    def open_user_guide(self):
        UserGuideWindow(self)


#Rum the application
app= Application()
app.mainloop()
