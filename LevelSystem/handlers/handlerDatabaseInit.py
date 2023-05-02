import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

def databaseInit():
    if settingBot.databaseType == "MariaDB":
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


    elif settingBot.databaseType == "SQLite":
        # Table of settings for the level system
        tableName = "addon_levelSystem_settings"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["channelID", "integer DEFAULT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # Table of users for the level system
        tableName = "addon_levelSystem_users"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["userID", "integer NOT NULL"],
            ["level", "integer DEFAULT 1"],
            ["xp", "integer DEFAULT 0"],
            ["lastJoin", "text DEFAULT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # Table of levels for the level system
        tableName = "addon_levelSystem_rewards"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["level", "integer NOT NULL"],
            ["roleID", "integer NOT NULL"],
            ["actionType", "integer NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)