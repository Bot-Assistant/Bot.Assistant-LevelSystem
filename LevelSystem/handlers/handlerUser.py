import services.serviceDatabase as serviceDatabase      

from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug


# Add user to the database  
def addUser(serverID, userID):
    requestFormat = """
                    INSERT INTO addon_levelSystem_users
                    (serverID, userID)
                    VALUES (%s, %s)
                    """
    requestSettings = (serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][ADD] Adding a user to the DB " + str(serverID) + " " + str(userID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][ADD] DB error addUser -> " + str(error))


# Delete user from the database
def deleteUser(serverID, userID):
    requestFormat = """
                    DELETE FROM addon_levelSystem_users
                    WHERE serverID = %s AND userID = %s;
                    """
    requestSettings = (serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][DELETE] Deleting a user from the DB " + str(userID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][DELETE] DB error deleteUser -> " + str(error))


# Get users from the database
def getAllUsers(serverID):
    requestFormat = """
                    SELECT *
                    FROM addon_levelSystem_users
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting users from the DB " + str(serverID))

        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getAllUsers -> " + str(error))


# Get user from the database
def getUser(serverID, userID):
    requestFormat = """
                    SELECT *
                    FROM addon_levelSystem_users
                    WHERE serverID = %s AND userID = %s
                    """
    requestSettings = (serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting a user from the DB " + str(serverID) + " " + str(userID))

        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getUser -> " + str(error))


# Update user level
def updateUserLevel(serverID, userID, level):
    requestFormat = """
                    UPDATE addon_levelSystem_users
                    SET level = %s
                    WHERE serverID = %s AND userID = %s;
                    """
    requestSettings = (level, serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][UPDATE] Updating a user level " + str(serverID) + " " + str(userID) + " " + str(level))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][UPDATE] DB error updateUserLevel -> " + str(error))


# Update user xp
def updateUserXP(serverID, userID, xp):
    requestFormat = """
                    UPDATE addon_levelSystem_users
                    SET xp = %s
                    WHERE serverID = %s AND userID = %s;
                    """
    requestSettings = (xp, serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][UPDATE] Updating a user xp " + str(serverID) + " " + str(userID) + " " + str(xp))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][UPDATE] DB error updateUserXP -> " + str(error))


# Set last join date
def addTimestamp(serverID, userID, timestamp):
    requestFormat = """
                    UPDATE addon_levelSystem_users
                    SET lastJoin = %s
                    WHERE serverID = %s AND userID = %s;
                    """
    requestSettings = (timestamp, serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][UPDATE] Updating a user timestamp " + str(serverID) + " " + str(userID) + " " + str(timestamp))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][UPDATE] DB error addTimestamp -> " + str(error))


# Get last join date
def getTimestamp(serverID, userID):
    requestFormat = """
                    SELECT lastJoin
                    FROM addon_levelSystem_users
                    WHERE serverID = %s AND userID = %s;
                    """
    requestSettings = (serverID, userID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting a user timestamp " + str(serverID) + " " + str(userID))
            
        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getTimestamp -> " + str(error))