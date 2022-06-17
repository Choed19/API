from dataclasses import dataclass
from getpass import getuser
from conDB import MyDB as db


class Action:
    def getUser():
        data = db.userAll()
        return data

    def getUserbyID(userID):
        data = db.getUserByID(userID)
        return data

    def getUserbyID2(userID):
        data = db.getUserbyID2(userID)
        return data

    def getUserByUsername(username):
        data = db.getUserByUsername(username)
        return data

    def addUser(user):
        ID = db.addUser(user)
        data = db.getUserByID(ID)
        return data
    
    def addUser2(user):
        ID = db.addUser2(user)
        data = db.getUserByID(ID)
        return data

    def addUser3(user):
        check = db.getUserByUsername(user.username)
        if(not check):
            ID = db.addUser2(user)
            data = db.getUserByID(ID)
            return data
        else:
            data = {"error":True, "user":"error"}

    def addUser2(user):
        ID = db.addUser2(user)
        data = db.getUserByID(ID)
        return data

    def login(user):

        getUser = db.login(user)
        if(getUser):
            data = getUser
        else:
            data = []
        return data
    
    def login_hw(password):
        getUser = db.login_hw(password)
        if(getUser):
            data = getUser
        else:
            data = []
        return data


    def changPassById(user):
        data = db.changPassById(user)
        if data[0]["error"] == False:
            getUser = db.getUserByID(user.ID)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def changPassHWById(ID, password_hw):
        data = db.changPassHWById(ID,password_hw)
        if data[0]["error"] == False:
            getUser = db.getUserByID(ID)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def changHistory(user):
        data = db.changHistory(user)
        if data[0]["error"] == False:
            getUser = db.getUserByID(user.ID)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def dleteUser(user):
        data = db.dleteUser(user)
        return data

    def dleteUserbyUsername(user):
        data = db.dleteUserbyUsername(user)
        return data

    def changPassByUsername(user):
        username = user.username
        password = user.password
        data = db.changPassByUsername(username, password)
        if data["error"] == False:
            getUser = db.getUserByUsername(username)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def getHW():
        data = db.getHW()
        return data

    def getHWByID(ID):
        data = db.getHWByID(ID)
        return data

    def getHWByName(name):
        data = db.getHWByName(name)
        return data

    def getHWByNameAndHWName(name, hw_name):
        data = db.getHWByNameAndHWName(name, hw_name)
        return data

    def addHW(name, hw_name):
        ID = db.addHW(name, hw_name)
        data = db.getHWByID(ID)
        return data

    def updateStatusHW(ID, status):
        error = db.updateStatusHW(ID, status)
        data = db.getHWByID(ID)
        return data

    def updateValueHW(ID, value):
        error = db.updateValueHW(ID, value)
        data = db.getHWByID(ID)
        return data

    def updateStatusAndValueHW(ID, status, value):
        error = db.updateStatusAndValueHW(ID, status, value)
        data = db.getHWByName(ID)
        return data

    def udeleteHW(ID):
        data = db.deleteHW(ID)
        return data
    
    def keypad(matrix_keys):
        data = db.getkeypad(matrix_keys)
        return data