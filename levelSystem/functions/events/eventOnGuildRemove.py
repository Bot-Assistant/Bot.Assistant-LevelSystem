import addons.LevelSystem.handlers.handlerSettings as handlerSettings

async def deleteServer(guild):
    server = handlerSettings.getServer(guild.id)
    if server == [(guild.id,)]:
        handlerSettings.deleteServer(guild.id)