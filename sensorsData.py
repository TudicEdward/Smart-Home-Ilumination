import random, time
from databaseServices.api import *
from datetime import datetime

# functions for setting the luxmeter value
def morning():
    sunrise = random.randint(300,400)
    return sunrise
def noon():
    midDay = random.randint(32000,100000)
    return midDay
def afternoon():
    daylight = random.randint(10000,25000)
    return daylight
def evening():
    sunset = random.randint(300,400)
    return sunset
def midnight():
    night = random.randint(0,1)
    return night
    

#callable functions for modifing data

#turn on light on movement detected
def movement_detected():
    value = 1
    timer = 60
    rooms = get_room_types()
    i= random.randint(0,len(rooms)-1)
    rows = get_lux_value(rooms[i][0])
    for row in rows:
        if row[0] < 500:
            update_sensor_movement(rooms[i][0],value)
            update_room_status(rooms[i][0],value)
            while timer:
                time.sleep(1)
                timer -= 1
            movement_undetected(rooms[i][0])    
            return 'OK',200
        else:
            return 'OK',200

#motions sensor does not detect movement anymore
def movement_undetected(room):
    value = 0
    update_sensor_movement(room,value)
    turn_off_lights(room,240)
    return 'OK',200

def turn_off_lights(room,timer):
    
    while timer:
        value = get_sensor_data(room)
        if(value[0][0] == 0):
            time.sleep(1)
            timer -= 1
        else:
            break
    update_room_status(room,0)
    
    

#update the value of luxmeter based on time of the day
def update_luxmeter():
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time >= '06:00:01' and current_time <= '08:00:00':
        data=morning()
    elif current_time >= '08:00:01' and current_time <= '11:00:00':
        data=afternoon()
    elif current_time >= '11:00:01' and current_time <= '15:00:00':
        data=noon()
    elif current_time >= '15:00:01' and current_time <= '20:00:00':
        data=afternoon()
    elif current_time >= '20:00:01' and current_time <= '22:00:00':
        data=evening()
    elif current_time >= '22:00:00' and current_time <= '06:00:00':
        data=midnight()
    update_sensor_luxmeter(data)
    return 'OK',200

