import services.serviceDatabase as serviceDatabase

def databaseInit():
    # Table of settings for the level system
    tableName = "addon_levelSystem_settings"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["channelID", "BIGINT DEFAULT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

    # Table of users for the level system
    tableName = "addon_levelSystem_users"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["userID", "BIGINT NOT NULL"],
        ["level", "INT DEFAULT 1"],
        ["xp", "INT DEFAULT 0"],
        ["lastJoin", "DATETIME DEFAULT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

    # Table of levels for the level system
    tableName = "addon_levelSystem_rewards"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["level", "INT NOT NULL"],
        ["roleID", "BIGINT NOT NULL"],
        ["actionType", "INT NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)