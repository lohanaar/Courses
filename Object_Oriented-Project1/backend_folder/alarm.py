#Import the modules
from datetime import datetime
import time

class Alarm:

    def __init__(self):
        pass

    #Convert the hour and minute into a datetime object for the current day
    def convert_datetime(self, hour_alarm: int, minute_alarm: int) -> datetime:
        current_date = datetime.now().date() #Get today's date
        #Combine today's date with the provided hour and minute to create a full datetime
        alarm = datetime.combine(current_date, datetime.min.time()).replace(hour=hour_alarm, minute=minute_alarm)
        return alarm

    #set the alarm that checks the current time until it matches the target alarm time
    def set_alarm (self, target: datetime):
        while True:
            current_time = datetime.now() #Gert the current time

            if current_time >= target: #if the current time is matches the alarm time, break the loop
                break

            time.sleep(1) #wait 1 sec to check again