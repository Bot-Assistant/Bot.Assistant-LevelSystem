# Addons imports
import addons.levelSystem.handlers.handlerUser as handlerUser
import addons.levelSystem.handlers.handlerSettings as handlerSettings

# Init BotAssistant
import services.serviceBot as serviceBot
bot = serviceBot.classBot.getBot()

async def onReady():

    for guild in bot.guilds:

        # Get all users from the database
        memberList = handlerUser.getAllUsers(guild.id)

        # Verify if all user in the server are in the database
        for member in guild.members:
            if member.id not in [member[2] for member in memberList]:
                if member.bot == False:
                    handlerUser.addUser(guild.id, member.id)

        # Verify if all user in the database are in the server
        for member in memberList:
            if member[2] not in [member.id for member in guild.members]:
                handlerUser.deleteUser(guild.id, member[2])

        # Verify if the server is in the database
        serverSetting = handlerSettings.getServer(guild.id)
        if serverSetting == []:
            handlerSettings.addServer(guild.id)

    # Verify if the bot is in servers in the database
    allServer = handlerSettings.getAllServers()
    for server in allServer:
        if server[0] not in [guild.id for guild in bot.guilds]:
            handlerSettings.deleteServer(server[0])
        

