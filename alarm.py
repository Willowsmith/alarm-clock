import datetime
import time
import json
import webbrowser
import random


def open_file():
    held_links = open('C://Users/Myssa/Desktop/alarm.json')
    data = json.load(held_links)
    item = random.choice(data)
    webbrowser.open_new(item)
   
    held_links.close()



def alarm(set_alarm_timer):
    current_time = datetime.datetime.now()
    the_now = current_time.strftime("%H:%M")
    while the_now != set_alarm_timer:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        print(now)
        if now == set_alarm_timer:
            open_file()
            break

def actual_time():
    set_alarm_timer = input("Please state hour and minute you wish to set the alarm for: ")
    alarm(set_alarm_timer)

actual_time()


