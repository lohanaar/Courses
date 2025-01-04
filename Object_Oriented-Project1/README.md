
# Diabetes App

This application was created as a college project to help manage diabetes by tracking glucose levels, carbohydrate intake, and insulin needs. It includes features like alarm setting and data summaries.

## Features

### 1. Insert Glucose/Carbs
- Input your blood glucose level and carbohydrate consumption.
- The app calculates the required insulin dose and saves the data to the database.

### 2. Generate Summary
- View summaries of glucose data for the last 3, 7, or 15 days.
- Displays:
  - **Average Glucose Level**.
  - **Time in Range**:
    - High: Glucose > 10 mmol/L.
    - In Range: 4 < Glucose ≤ 10 mmol/L.
    - Low: Glucose ≤ 4 mmol/L.

### 3. Set Alarm
- Schedule an alarm for reminders to check glucose levels.
- If the time entered has already passed, a warning message box appears.

## How to Use

### Main Window
- **Insert Glucose/Carbs**: Opens a window to input glucose and carbs data.
- **Generate Summary**: Opens a window to generate glucose data summaries.
- **New Alarm**: Opens a window to set a new alarm.
- **Help**: Opens a user guide.

### Database Handling
- If no glucose data exists, an error message box is displayed: "There is no data available! You must insert glucose/carbs first."

### User Guide
A detailed guide is available within the app to explain all features.

## Technologies Used
- **Python**: Core language.
- **SQLite**: Database for storing glucose and insulin data.
- **Tkinter**: GUI framework for creating the interface.

## Requirements

- Python 3.x
- Tkinter 
- SQLite 

## License

This is created for educational purposes and is freely available for non-commercial use.

### Notes
- Ensure all values are entered accurately for reliable insulin recommendations.
- The database file `DiabetesApp.db` was added to the project with mock data (dated from 18/12/2024 to 21/01/2025) in order to test the app. If you want to use as a new user, you can delete this file and a new one will be generated.

---

## References

1. Python Software Foundation. (2023). Python 3 documentation. Retrieved from https://docs.python.org/3/

2. TkDocs. (n.d.). Tkinter tutorial. Retrieved from https://tkdocs.com/tutorial/

3. Python Software Foundation. (2023). Tkinter documentation. Retrieved from https://docs.python.org/3/library/tkinter.html

4. SQLite Consortium. (2023). SQLite documentation. Retrieved from https://www.sqlite.org/docs.html

5. Python Software Foundation. (2023). sqlite3 — DB-API 2.0 interface for SQLite databases. Retrieved from https://docs.python.org/3/library/sqlite3.html

6. Python Software Foundation. (2023). Errors and exceptions. Retrieved from https://docs.python.org/3/tutorial/errors.html

7. Python Software Foundation. (2020). PEP 8 -- Style Guide for Python Code. Retrieved from https://peps.python.org/pep-0008/

