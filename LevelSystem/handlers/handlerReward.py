import services.serviceDatabase as serviceDatabase      

from services.serviceLogger import Logger
from settings.settingBot import debug


# Add a new reward to the database
def addReward(serverID, level, roleID, actionType):
    requestFormat = """
                    INSERT INTO addon_levelSystem_rewards
                    (serverID, level, roleID, actionType)
                    VALUES (%s, %s, %s, %s)
                    """
    requestSettings = (serverID, level, roleID, actionType,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][ADD] Adding a reward to the DB " + str(serverID) + " " + str(level) + " " + str(roleID) + " " + str(actionType))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][ADD] DB error addReward -> " + str(error))


# Delete a reward from the database
def deleteReward(serverID, level, roleID):
    requestFormat = """
                    DELETE FROM addon_levelSystem_rewards
                    WHERE serverID = %s AND level = %s AND roleID = %s;
                    """
    requestSettings = (serverID, level, roleID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][DELETE] Deleting a reward from the DB " + str(serverID) + " " + str(level) + " " + str(roleID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][DELETE] DB error deleteReward -> " + str(error))


# Get all rewards from the database
def getAllRewards(serverID):
    requestFormat = """
                    SELECT *
                    FROM addon_levelSystem_rewards
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting rewards from the DB " + str(serverID))

        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getAllRewards -> " + str(error))


# Get all rewards levels from the database
def getRewardLevels(serverID):
    requestFormat = """
                    SELECT level
                    FROM addon_levelSystem_rewards
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting all rewards levels from the DB " + str(serverID))

        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getRewardLevels -> " + str(error))


# Get all rewards roles from a level from the database
def getRewardRoles(serverID, level):
    requestFormat = """
                    SELECT roleID, actionType
                    FROM addon_levelSystem_rewards
                    WHERE serverID = %s AND level = %s
                    """
    requestSettings = (serverID, level,)
    try:
        Logger.debug("[HANDLER][LEVELSYSTEM][GET] Getting all rewards roles from a level from the DB " + str(serverID) + " " + str(level))

        return serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][LEVELSYSTEM][GET] DB error getRewardRoles -> " + str(error))