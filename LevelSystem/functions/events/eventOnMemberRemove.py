import addons.LevelSystem.handlers.handlerUser as handlerUser

# Delete user from the database from the event
async def deleteUser(member):
    if member.bot == False:
        handlerUser.deleteUser(member.guild.id, member.id)
