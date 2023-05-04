import datetime

import addons.LevelSystem.handlers.handlerUser as handlerUser
import addons.LevelSystem.handlers.handlerReward as handlerReward
import addons.LevelSystem.handlers.handlerSettings as handlerSettings

from services.serviceDiscordLogger import discordLogger as DiscordLogger

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def addXPVoice(member, before, after):
    
    # If the user connects to a voice channel that is not the afk channel
    # If the user join a channel and leave the afk channel
    if before.channel == None and after.channel != None and after.afk != True or before.afk == True and after.afk == False:

        # Get the date
        timestamp = datetime.datetime.now()

        # Add the date to the database
        handlerUser.addTimestamp(member.guild.id, member.id, timestamp)


    # If the user disconnects from a voice channel that is not the afk channel
    # If the user leave a channel and join the afk channel
    elif before.channel != None and after.channel == None and before.afk != True or before.afk == False and after.afk == True:

        # Get the date from the database
        try:
            timestampDB = handlerUser.getTimestamp(member.guild.id, member.id)[0]
        except:
            return

        # If timestamp is None, return
        if timestampDB[0] is None:
            return

        # If timestamp is a string, convert it to datetime
        if isinstance(timestampDB[0], str):
            timestampDate = datetime.datetime.strptime(timestampDB[0], "%Y-%m-%d %H:%M:%S.%f")
        else:
            timestampDate = timestampDB[0]

        # Remove the date from the database
        handlerUser.addTimestamp(member.guild.id, member.id, None)

        # Calculate the time difference to get the xp earned
        timeDifference = datetime.datetime.now() - timestampDate
        xp = timeDifference.seconds / 60
        xp = round(xp)

        # Get the user data
        userData = handlerUser.getUser(member.guild.id, member.id)[0]

        # Extract the user data
        userLevel = userData[3]
        userXP = userData[4]

        # Calculate the new XP
        newLevelXP = userXP + xp
        nextLevelXP = userLevel * 100

        # Check if the user has leveled up
        if newLevelXP >= nextLevelXP:

            channel = handlerSettings.getChannelID(member.guild.id)[0][0]
            channel = member.guild.get_channel(channel)

            newUserLevel = userLevel + 1

            handlerUser.updateUserLevel(member.guild.id, member.id, newUserLevel)
            handlerUser.updateUserXP(member.guild.id, member.id, 0)

            #Embed message to inform the user that he has leveled up
            embed = discord.Embed(
                title="Level Up!",
                description=f"{member.mention} has leveled up to level {newUserLevel}!",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.display_avatar)
            embed.set_footer(text=f"Make command `/levelsystem level` to see your level")

            # Check if the user has a reward for leveling up
            rewardLevelsDatabase = handlerReward.getRewardRoles(member.guild.id, newUserLevel)

            if channel is None:
                DiscordLogger.error(f"LevelSystem: You need to set a channel for the level system. Use the command `/levelsystem settings channel` to set a channel.")
            
            else:
                # Check if the bot has permissions to manage roles
                if channel.guild.me.guild_permissions.manage_roles == False:
                    embed.add_field(name="Error", value="The bot does not have permissions to manage roles")
                    await channel.send(embed=embed)
                    return


            # Make a list of the roles rewards
            rewardRoles = []
            for rewardLevel in rewardLevelsDatabase:
                    
                    # If the role is not find, it will be deleted from the database
                    if member.guild.get_role(rewardLevel[0]) is None:
                        handlerReward.deleteReward(member.guild.id, newUserLevel, rewardLevel[0])
                    else:
                        rewardRoles.append([member.guild.get_role(rewardLevel[0]), rewardLevel[1]])

            for rewardRole in rewardRoles:
                if rewardRole[1] == 1:
                    await member.add_roles(rewardRole[0])
                    embed.add_field(name="New Role", value=f"{rewardRole[0].mention}")
                else:
                    await member.remove_roles(rewardRole[0])
                    embed.add_field(name="Removed Role", value=f"{rewardRole[0].mention}")

            await channel.send(embed=embed)
        
        else:
            handlerUser.updateUserXP(member.guild.id, member.id, newLevelXP)
            

        
