DB_Tables = []

class Table:

    insertString = "CREATE TABLE {tableName} ("

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def getQuerry(self):
        res = self.insertString.format(tableName=self.name)
        for columns in self.columns:
            res += columns.getQuerry() + ", "
        res = res[:-2]
        res += ")"
        return res


class Column:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def getQuerry(self):
        return "{name} {datatype}".format(name=self.name,
                                          datatype=self.datatype)

# create the table Lightbulbs
DB_Tables.append(
    Table("Lightbulb",(
        Column("ID","INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL"),
        Column("status","INTEGER NOT NULL"),
        Column("power","FLOAT NOT NULL"),
        Column("color","TEXT NOT NULL"),
        Column("turned_on","DATETIME "),
        Column("turned_off","DATETIME "),
        Column("time_on","DATETIME DEFAULT '0'")
    ))
)

# create the table Rooms
DB_Tables.append(
    Table("Rooms",(
        Column("type","TEXT NOT NULL"),
        Column("lightbulbID","INTEGER NOT NULL"),
        Column("lightbulb_consumption","FLOAT DEFAULT '0'"),
        Column("","FOREIGN KEY ('lightbulbID') REFERENCES 'Lightbulb' ('ID') ON DELETE CASCADE ON UPDATE CASCADE"),
        Column("","FOREIGN KEY ('type') REFERENCES 'House' ('room_type') ON DELETE CASCADE ON UPDATE CASCADE")
    ))
)

# create the table Sensors
DB_Tables.append(
    Table("Sensors",(
        Column("ID","INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL"),
        Column("room_type","INTEGER NOT NULL"),
        Column("type","TEXT NOT NULL"),
        Column("value","FLOAT DEFAULT '0'"),
        Column("","FOREIGN KEY ('room_type') REFERENCES 'House' ('room_type') ON DELETE CASCADE ON UPDATE CASCADE")
    ))
)

# create the table House
DB_Tables.append(
    Table("House",(
        Column("room_type","TEXT PRIMARY KEY NOT NULL"),
        Column("status","INTEGER NOT NULL"),
        Column("room_consumption","FLOAT DEFAULT '0'"),
        Column("color","TEXT NOT NULL")
    ))
)

# create the table Users
DB_Tables.append(
    Table("Users",(
        Column("ID", "INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL"),
        Column("username", "TEXT NOT NULL"),
        Column("password", "TEXT NOT NULL")
    ))
)

#create the table Preferences
DB_Tables.append(
    Table("Preferences",(
        Column("user_id", "INTEGER NOT NULL"),
        Column("leave_work", "TIME NOT NULL"),
        Column("arrive_work", "TIME NOT NULL"),
        Column("","FOREIGN KEY ('user_id') REFERENCES 'Users' ('ID') ON DELETE CASCADE ON UPDATE CASCADE")
    ))
)

#create the table Auth
DB_Tables.append(
    Table("Auth",(
        Column("username", "INTEGER NOT NULL"),
        Column("token", "TEXT NOT NULL"),
    ))
)


