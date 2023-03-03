import addons.levelSystem.handlers.handlerUser as handlerUser

# Add user to the database from the event
async def addUser(member):
    if member.bot == False:
        handlerUser.addUser(member.guild.id, member.id)
