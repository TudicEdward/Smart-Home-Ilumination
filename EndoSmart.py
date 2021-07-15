from sensorsData import movement_detected, update_luxmeter
from flask import Flask,render_template,jsonify,request,redirect,send_from_directory
from databaseServices.api import *
import os, random, threading,time


app = Flask(__name__)

def generate_token(length):
    result_str = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for i in range(length))
    return result_str

def end_sesion(timer,username):
    while timer:
        time.sleep(1)
        timer -= 1
    delete_auth(username)
    return redirect('/')

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(update_luxmeter, 300)
set_interval(movement_detected, 360)



# Functions for inserting information


# insert new room in the house
@app.route('/inserthouseroom', methods=['POST'])
def inserthouseroom():
    if request.method=="POST":
        type = request.form["roomtype"]
        insert_house_room(type)
        return redirect('/') 

# insert new lightbulb in a specific room
@app.route('/insertroomlight', methods=['POST'])
def insertroomlight():
    if request.method=="POST":
        bulb = request.form["selectbulbs"]
        room = request.form["room_type"]
        insert_room_light(room,bulb)
        return redirect('/') 

# insert new lightbulb
@app.route('/insertbulb', methods=['POST'])
def insertbulb():
    if request.method=="POST":
        insert_lightbulb()
        return redirect('/') 

# insert new user
@app.route('/insertuser', methods=['POST'])
def insertuser():
    if request.method=="POST":
        user = request.form["username"]
        passwd = request.form["password"]
        insert_user(user,passwd)
        return redirect('/') 

# insert new sensor
@app.route('/insertsensor', methods=['POST'])
def insertsensor():
    if request.method=="POST":
        room = request.form["room_types"]
        senz = request.form["senstype"]
        insert_sensors(room,senz)
        return redirect('/') 

@app.route('/insertpreferences', methods=['POST'])
def insertpreferences():
    if request.method=="POST":
        id = get_auth_id()
        leave = request.form["leave"]
        arrive = request.form["arrive"]
        insert_preferences(id[0][0], leave, arrive)
        return redirect('/') 



# Functions for deleteing information



# delete a room from the house
@app.route('/deletehouseroom', methods=['POST'])
def deletehouseroom():
    if request.method=="POST":
        type = request.form["house_room_type"]
        delete_house_room(type)
        return redirect('/') 

# delete a lightbulb from a specified room  
@app.route('/deleteroomlight', methods=['POST'])
def deleteroomlight():
    if request.method=="POST":
        type = request.form["house_room_types"]
        id = request.form["bulb_id"]
        delete_room_light(type,id)
        return redirect('/') 

# delete a lightbulb
@app.route('/deletebulb', methods=['POST'])
def deletebulb():
    if request.method=="POST":
        bulb = request.form["lightbulb_id"]
        delete_lightbulb(bulb)
        return redirect('/') 

# delete a user
@app.route('/deleteuser', methods=['POST'])
def deleteuser():
    if request.method=="POST":
        user = request.form["user_name"]
        delete_user(user)
        return redirect('/') 

# delete a sensor
@app.route('/deletesensor', methods=['POST'])
def deletesensor():
    if request.method=="POST":
        senz = request.form["sens_id"]
        delete_sensor(senz)
        return redirect('/') 



# Functions for updateing information



# update the status of a specified room
@app.route('/updateroomstatus', methods=['POST'])
def updateroomstatus():
    if request.method=="POST":
        data=request.get_json()
        update_room_status(data[0],data[1])
        if data[1] == 0:
            update_time_on_room(data[0])
        return 'OK',200

# update the status of a specified bulb
@app.route('/updateroombulbstatus', methods=['POST'])
def updateroombulbstatus():
    if request.method=="POST":
        data=request.get_json()
        update_bulb_status(data[0],data[1])
        if data[1] == 0:
            update_time_on_bulb(data[0])
        return 'OK',200

# update the color of lightbulbs
@app.route('/updatelightbulbcolor', methods=['POST'])
def updatelightbulbcolor():
    if request.method=="POST":
        data=request.get_json()
        update_lightbulbs_color(data[0],data[1])
        return 'OK',200

@app.route('/updatebulbconsumption')
def updatebulbconsumption():
    rows = get_lightbulb_time_on()
    for data in rows:
        value = (60/1000)*data[1]
        update_bulb_consumption(data[0],value)
    return 'OK',200

@app.route('/updateroomconsumption')
def updateroomconsumption():
    value = 0
    array = []
    rows = get_room_consumption()
    for i in rows:
        if i[0] not in array:
            array.append(i[0])
    for data in array:
        for val in rows:
            if(data[0]==val[0]):
                value += val[1]
        value = 0
        update_room_consumption(data[0],value)
    array = []
    return 'OK',200





# Functions for gethering information



# get all the rooms from the house with some data
@app.route('/getrooms')
def getRooms():
    rows=get_house_rooms()
    return jsonify(rows)

# get all the lights in the house
@app.route('/roomlights')
def getRoomData():
    rows = get_room_lights()
    return jsonify(rows)

# gets the unsigned lightbulbs
@app.route('/getunsignedbulbs')
def getunsignedbulbs():
    rows=get_unsigned_bulbs()
    return jsonify(rows)

# gets the rooms from the house
@app.route('/getroomtypes')
def getroomstypes():
    rows=get_room_types()
    return jsonify(rows)

# gets the ids of all the sensors
@app.route('/getsensorids')
def getsensorids():
    rows=get_sensor_ids()
    return jsonify(rows)

# gets the ids of all asigned lightbulbs
@app.route('/getbulbsid')
def getbulbsid():
    rows=get_bulbs_ids()
    return jsonify(rows)

# gets all the usernames
@app.route('/getusernames')
def getusernames():
    rows=get_user_names()
    return jsonify(rows)

# gets the rooms with lightbulbs from house
@app.route('/gethouserooms')
def gethouserooms():
    rows=get_houserooms()
    return jsonify(rows)

# gets the ids of all lightbulbs
@app.route('/getlightbulbids')
def getlightbulbids():
    rows=get_lightbulb_ids()
    return jsonify(rows)

@app.route('/getroomasignedbulbs')
def getroomasignedbulbs():
    rows=get_room_asigned_bulbs()
    return jsonify(rows)



# Root functions and Login



@app.route('/')
def index():
    valid = check_auth()
    if(valid[0][0] == 1):
        return render_template('Server.html')
    else:
        return render_template('Login.html')

@app.route('/', methods=['POST'])
def login():
    if request.method=="POST":
        usrn = request.form["username"]
        passwd = request.form["password"]
        rows = check_user(usrn, passwd)
        if(rows[0][0] == 1):
            token = generate_token(20)
            insert_auth(usrn,token)
            #end_sesion(1800,usrn)
            return redirect('/') 
        else:
            return redirect('/')
    else:
            return redirect('/')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    initialize_database()
    app.debug=True
    app.run()