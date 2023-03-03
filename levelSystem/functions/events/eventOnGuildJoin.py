import addons.LevelSystem.handlers.handlerSettings as handlerSettings

async def addServer(guild):
    server = handlerSettings.getServer(guild.id)
    if server == []:
        handlerSettings.addServer(guild.id)