import services.serviceDatabase as serviceDatabase      

from services.serviceLogger import Logger
from settings.settingBot import debug

# Add server to the database
def addServer(serverID):
    requestFormat = """
                    INSERT INTO addon_levelSystem_settings (serverID)
                    VALUES (%s);
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][ADD] Adding server to the DB " + str(serverID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][ADD] DB error addServer -> " + str(error))


# Delete server from the database
def deleteServer(serverID):
    requestFormat = """
                    DELETE FROM addon_levelSystem_settings
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][DEL] Deleting server from the DB " + str(serverID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][DEL] DB error deleteServer -> " + str(error))


# Get server from the database
def getServer(serverID):
    requestFormat = """
                    SELECT serverID
                    FROM addon_levelSystem_settings
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting server from the DB " + str(serverID))
            
        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getServer -> " + str(error))


# Get all servers from the database
def getAllServers():
    requestFormat = """
                    SELECT serverID
                    FROM addon_levelSystem_settings
                    """
    requestSettings = ()
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting all servers from the DB")
            
        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getAllServers -> " + str(error))


# Set channel id for the addon in the database
def setChannelID(serverID, channelID):
    requestFormat = """
                    UPDATE addon_levelSystem_settings
                    SET channelID = %s
                    WHERE serverID = %s;
                    """
    requestSettings = (channelID, serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][SET] Setting channelID to the DB " + str(serverID) + " " + str(channelID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][SET] DB error setChannelID -> " + str(error))


# Get channel id for the addon from the database
def getChannelID(serverID):
    requestFormat = """
                    SELECT channelID
                    FROM addon_levelSystem_settings
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting channelID from the DB " + str(serverID))
            
        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getChannelID -> " + str(error))