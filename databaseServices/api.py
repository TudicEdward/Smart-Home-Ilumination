import sqlite3
from databaseServices.dbTables import *
from databaseServices.extraTools import *

DATABASE_LINK = 'lighting.db'

def foreignKey(connection):
    connection.execute("PRAGMA foreign_keys=ON")

# database initialization
def createDatabaseAndTables():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            foreignKey(DB)
            log("Database created")
            for table in DB_Tables:
                try:
                    DB.execute(table.getQuerry())
                    log("Table {name} created".format(name=table.name))
                except Exception as e:
                    log("Error creating table {name} with error: {err}".format(
                        name=table.name, err=str(e)))
    except Exception as e:
        log("Error creating database: " + str(e))


# Insert functions


# inserts lightbulb in a specified room
def insert_room_light(type, lightbulbID):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("INSERT INTO 'Rooms'('type','lightbulbID') VALUES(?,?)",(type,lightbulbID,))
            DB.commit()
            log("Data was inserted")
    except Exception as e:
        log("Data insertion failed")

# insert new lightbulb
def insert_lightbulb():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("INSERT INTO 'Lightbulb'('status','power','color') VALUES(?,?,?)",("0","0","#ffffff",))
            DB.commit()
            log("Data was inserted")
    except Exception as e:
        log("Data insertion failed")

# insert sensor for specific room
def insert_sensors(room_type,type):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""INSERT INTO 'Sensors'('room_type','type') VALUES(?,?);""",(room_type,type,))
            DB.commit()
            log("Data was inserted")
    except Exception as e:
        log("Data insertion failed")

# insert room in the house
def insert_house_room(type):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""INSERT INTO 'House'('room_type','status','color') VALUES(?,?,?)""",(type,"0","#ffffff",))
            DB.commit()
            log("Data was inserted")
    except Exception as e:
        log("Data insertion failed")

# insert new user
def insert_user(username,password):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""INSERT INTO 'Users'('username','password') VALUES(?,?)""",(username,password,))
            DB.commit()
            log("Data was inserted")
    except Exception as e:
        log("Data insertion failed")

def insert_auth(user,token):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""INSERT INTO 'Auth' VALUES(?,?)""",(user,token,))
            DB.commit()
            log("User authenticated")
    except Exception as e:
        log("User could not be authenticated")

def insert_preferences(id, leave, arrive):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            result = check_preference(id)
            if(result[0][0] == 1):
                update_preferences(id, leave, arrive)
            else:
                DB.execute("""INSERT INTO 'Preferences' VALUES(?,?,?)""",(id,leave,arrive,))
                DB.commit()
            log("User authenticated")
    except Exception as e:
        log("User could not be authenticated")
# Delete functions


# delete lightbulb from specified room
def delete_room_light(type,id):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'Rooms' WHERE type = ? AND lightbulbID = ?""",(type,id,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")

# delete room from house
def delete_house_room(type):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'House' WHERE room_type = ?""",(type,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")

# delete specified lightbulb
def delete_lightbulb(id):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'Lightbulb' WHERE ID = ?""",(id,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")

# delete specified sensor
def delete_sensor(id):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'Sensors' WHERE ID = ?""",(id,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")

# delete specified user
def delete_user(username):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'Users' WHERE username = ?""",(username,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")

#delete the sesion from auth
def delete_auth(username):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""DELETE FROM 'Auth' WHERE username = ?""",(username,))
            DB.commit()
            log("Data was deleted")
    except Exception as e:
        log("Data deletion failed")



# Update functions


# update the status of specified room
def update_room_status(type,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE House SET status = ? WHERE room_type = ?""",(value,type,))
            DB.commit()
            if value == 1:
                DB.execute("""UPDATE Lightbulb SET status=?,turned_on=(SELECT datetime()) WHERE ID in (SELECT lightbulbID FROM Rooms WHERE type=?)""",(value,type,))
                DB.commit()
            else:
                DB.execute("""UPDATE Lightbulb SET status=?,turned_off=(SELECT datetime()) WHERE ID in (SELECT lightbulbID FROM Rooms WHERE type=?)""",(value,type,))
                DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

# update the status of a specified bulb
def update_bulb_status(id,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            if value == 1:
                DB.execute("""UPDATE Lightbulb SET status=?,turned_on=(SELECT datetime()) WHERE ID = ?""",(value,type,))
                DB.commit()
            else:
                DB.execute("""UPDATE Lightbulb SET status=?,turned_off=(SELECT datetime()) WHERE ID = ?""",(value,type,))
                DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")  

# update the color of lightbulbs
def update_lightbulbs_color(room,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE House SET color = ? WHERE room_type = ?""",(value,room,))
            DB.commit()
            DB.execute("""UPDATE Lightbulb SET color=? WHERE ID in (SELECT lightbulbID FROM Rooms WHERE type=?)""",(value,room,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

# update consumption of lightbulbs
def update_bulb_consumption(id,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE Rooms SET lightbulb_consumption = ? WHERE lightbulbID = ?""",(value,id,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

# update total room consumption 
def update_room_consumption(room,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE House SET room_consumption = ? WHERE room_type = ?""",(value,room,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

def update_sensor_movement(room,value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE Sensors SET value = ? WHERE room_type = ? AND type = 'movement'""",(value,room,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

def update_sensor_luxmeter(value):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            rows = get_room_types()
            for row in rows:
                DB.execute("""UPDATE Sensors SET value = ? WHERE room_type = ? AND type = 'luxmeter'""",(value,row[0],))
                DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

def update_time_on_room(room):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE Lightbulb SET time_on = (SELECT time_on FROM Lightbulb WHERE ID in (SELECT lightbulbID FROM Rooms WHERE type = ?)) + (SELECT strftime('%M',turned_off)-strftime('%M',turned_on) FROM Lightbulb ) WHERE ID in (SELECT lightbulbID FROM Rooms WHERE type = ?) """,(room,room,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

def update_time_on_bulb(bulb):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE Lightbulb SET time_on = (SELECT time_on FROM Lightbulb WHERE ID = ?) + (SELECT strftime('%M',turned_off)-strftime('%M',turned_on) FROM Lightbulb ) WHERE ID = ? """,(bulb,bulb,))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

def update_preferences(id, leave, arrive):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            DB.execute("""UPDATE Preferences SET leave_work = ?, arrive_work = ? WHERE user_id = ? """,(leave, arrive, id))
            DB.commit()
            log("Data updated")
    except Exception as e:
        log("Data could not be updated")

# Gettering functions


# get all the rooms from the house with some data
def get_house_rooms():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT room_type,status,room_consumption,color FROM House")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# get all the lights in the house
def get_room_lights():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT Lightbulb.status, Lightbulb.color, Rooms.type FROM 'Lightbulb' INNER JOIN 'ROOMS' ON Rooms.lightbulbID = Lightbulb.ID")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the unsigned lightbulbs
def get_unsigned_bulbs():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT Lightbulb.ID FROM Lightbulb LEFT JOIN Rooms on Rooms.lightbulbID = Lightbulb.ID WHERE Rooms.lightbulbId is NULL")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the rooms from the house
def get_room_types():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT room_type FROM House ")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the ids of all the sensors
def get_sensor_ids():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT ID FROM Sensors ")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

def get_sensor_data(room):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT value FROM Sensors WHERE room_type = ? AND type = 'movement'")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the ids of all lightbulbs
def get_lightbulb_ids():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT ID FROM Lightbulb ")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets all the usernames
def get_user_names():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT username FROM Users ")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the ids of all asigned lightbulbs
def get_bulbs_ids():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT type,lightbulbID FROM Rooms")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the rooms with lightbulbs from house
def get_houserooms():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT type FROM Rooms ")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")

# gets the bulbs and their data for all rooms
def get_room_asigned_bulbs():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT Rooms.type, Lightbulb.ID,Lightbulb.status FROM Lightbulb INNER JOIN Rooms on Lightbulb.ID = Rooms.lightbulbID")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")  

# gets the time that each lightbulb was on
def get_lightbulb_time_on():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT ID, time_on FROM Lightbulb WHERE time_on NOT NULL")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")  

def get_room_consumption():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT type, lightbulb_consumption FROM Rooms WHERE lightbulb_consumption NOT NULL")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")  

def get_lux_value(room):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT value FROM Sensors WHERE room_type = ? AND type = 'luxmeter'",(room,))
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed") 

def get_auth_id():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT ID FROM Users WHERE username = (SELECT username from Auth)")
            result = cursor.fetchall()
            cursor.close()
            log("Data collected")
            return result
    except Exception as e:
        log("Data collecting failed")    
  


# check if user exists
def check_user(username,password):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT count() FROM Users WHERE username = ? and password = ?",(username, password))
            result = cursor.fetchall()
            cursor.close()
            log("User exists")
            return result
    except Exception as e:
        log("User does not exist")

def check_auth():
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT count() FROM Auth ")
            result = cursor.fetchall()
            cursor.close()
            log("User is logged")
            return result
    except Exception as e:
        log("User is not login")

def check_preference(id):
    try:
        with sqlite3.connect(DATABASE_LINK) as DB:
            cursor = DB.cursor()
            cursor.execute("SELECT count() FROM Preferences WHERE user_id = ?",(id,))
            result = cursor.fetchall()
            cursor.close()
            log("Data colected")
            return result
    except Exception as e:
        log("Data could not be colected")




def initialize_database():
    createDatabaseAndTables()
