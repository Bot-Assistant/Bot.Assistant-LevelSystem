import addons.LevelSystem.handlers.handlerUser as handlerUser
import addons.LevelSystem.handlers.handlerReward as handlerReward

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def addXPMessage(message):

    # Check if the message is from a bot
    if message.author.bot:
        return

    # Check if the message is from a private channel
    if message.guild is None:
        return
    
    # Get the user data from the database
    userData = handlerUser.getUser(message.guild.id, message.author.id)[0]

    # Extract the user data
    userLevel = userData[3]
    userXP = userData[4]

    # Calculate the new XP
    messageScore = 0

    # Calculate the score of the message
    for word in message.content.split():
        if message.content.count(word) == 1:
            messageScore += 1
        else:
            messageScore += 1 / message.content.count(word)

    newLevelXP = userXP + messageScore
    round(newLevelXP)
    nextLevelXP = userLevel * 100

    # Check if the user has leveled up
    if newLevelXP >= nextLevelXP:

        # Calculate the new level
        newUserLevel = userLevel + 1

        # Update the user data in the database
        handlerUser.updateUserLevel(message.guild.id, message.author.id, newUserLevel)
        handlerUser.updateUserXP(message.guild.id, message.author.id, 0)
        
        # Create the embed
        embed = discord.Embed(
            title="Level Up!",
            description=f"{message.author.mention} has leveled up to level {newUserLevel}!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=message.author.display_avatar)
        embed.set_footer(text=f"Make command `/levelsystem level` to see your level")

        # Check if the user has a reward for leveling up
        rewardLevelsDatabase = handlerReward.getRewardRoles(message.guild.id, newUserLevel)

        # Check if the bot has permissions to manage roles
        if not message.guild.me.guild_permissions.manage_roles:
            embed.add_field(name="Error", value="The bot does not have permissions to manage roles. ")
            await message.channel.send(embed=embed)
            return

        # Make a list of the roles rewards
        rewardRoles = []

        # Check if the role is find
        for rewardLevel in rewardLevelsDatabase:
            if message.guild.get_role(rewardLevel[0]) is None:
                handlerReward.deleteReward(message.guild.id, newUserLevel, rewardLevel[0])
            else:
                rewardRoles.append([message.guild.get_role(rewardLevel[0]), rewardLevel[1]])

        # Give the rewards to the user
        for rewardRole in rewardRoles:
            if rewardRole[1] == 1:
                await message.author.add_roles(rewardRole[0])
                embed.add_field(name="New Role", value=f"{rewardRole[0].mention}")
            else:
                await message.author.remove_roles(rewardRole[0])
                embed.add_field(name="Removed Role", value=f"{rewardRole[0].mention}")

        # Send the embed
        await message.channel.send(embed=embed)

    else:
        handlerUser.updateUserXP(message.guild.id, message.author.id, newLevelXP)