import pyautogui as pg
import subprocess
from time import sleep 
import datetime
from datetime import date
import calendar
from schedule import *
from classes import *

zoom_path = r'C:\Users\siddh\AppData\Roaming\Zoom\bin\Zoom.exe'#path to the zoom app

class Bot():
    def __init__(self,zoom_path,end_time):
        self.path = zoom_path
        self.a_classes = a_day
        self.b_classes = b_day
        self.classes = a_day + b_day
        self.times = []
        self.get_times()
        self.end_time = end_time

        self.a_times_to_classes = {}
        self.b_times_to_classes = {}
        self.create_times_dict()

    def join_meeting(self,id, password = None):
        subprocess.Popen(self.path)#open zoom
        sleep(1.7)
        pg.click('imgs/Screenshot 2021-01-13 133019.png')
        sleep(3)
        pg.write(id)
        pg.click('imgs/join button.png')
        sleep(3)
        if password is not None:
            try:
                pg.write(password)
            except:
                pass
        sleep(1)
        try:
            pg.click('imgs/join 2.png')
            sleep(2)
        except:
            pass 
        try:
            pg.click('imgs/no video.png')
        except:
            pass
    
    def check_time(self,hour,minute):
        hour_true = (datetime.datetime.now().hour == hour)
        minute_true = (datetime.datetime.now().minute == minute)
        #second_true = (datetime.datetime.now().second == 0)

        if minute == None:
            minute_true = True

        if(hour_true and minute_true):
            return True
        return False

    def get_day(self):
        my_date = date.today()
        return calendar.day_name[my_date.weekday()] 
    
    def a_or_b(self):
        if self.get_day() == 'Monday' or self.get_day() == 'Wendsday':
            return 0
        elif self.get_day() == 'Tuesday' or self.get_day() == 'Thursday':
            return 1 
        return 0

    def get_times(self):
        for c in self.classes:
            self.times.append(c.time)

    def main(self):
        if self.a_or_b() == 0:
            for c in self.a_classes:
                if self.check_time(c.time.hours, c.time.minutes):
                    curr_creds = str(c.get_credentials())
                    curr_id = curr_creds[1:curr_creds.find(',')]
                    curr_password = curr_creds[curr_creds.find(',')+1:-1]
                    self.join_meeting(curr_id,curr_password)
        elif self.a_or_b() == 1:
            for c in self.b_classes:
                if self.check_time(c.time.hours, c.time.minutes):
                    curr_creds = str(c.get_credentials())
                    curr_id = curr_creds[1:curr_creds.find(',')]
                    curr_password = curr_creds[curr_creds.find(',')+1:-1]
                    self.join_meeting(curr_id,curr_password)


    def create_times_dict(self):
        for c in self.a_classes:
            self.a_times_to_classes[c.time] = c 
        
        for c in self.b_classes:
            self.b_times_to_classes[c.time] = c 

b = Bot(zoom_path,Timestamp(17,1))
while True:
    b.main()
    if(b.check_time(b.end_time.hours,b.end_time.minutes)):
        break