import datetime
from datetime import date
import calendar

class Timestamp():
    def __init__(self,hours,minutes):
        self.hours = int(hours) 
        self.minutes = int(minutes) 
        self.format()

    def format(self):
        if self.minutes is not None:
            if int(self.minutes) > 60:
                self.minutes -= 60
                self.hours +=1 
    

class Class():
    def __init__(self,time,credentials_deafault,
                credentials_monday = None,
                credentials_tuesday = None,
                credentials_wendsay = None,
                credentials_thurday = None,
                credentials_friday = None):
        
        self.time = time
        self.credentials = [credentials_monday,credentials_tuesday,credentials_wendsay,credentials_thurday,credentials_friday,credentials_deafault] 
        self.create_credentials()

    def create_credentials(self):
        classes = {}
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Default']
        for i in range(len(self.credentials)):
            classes[days[i]] = self.credentials[i]
        self.credentials = classes


    def get_day(self):
        my_date = date.today()
        return calendar.day_name[my_date.weekday()] 
    
    def get_credentials(self):
        if len(str(self.credentials[self.get_day()]))>3:
            return self.credentials[self.get_day()]
        return self.credentials['Default']
    


