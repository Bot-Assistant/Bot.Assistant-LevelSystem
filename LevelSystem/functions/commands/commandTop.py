import addons.LevelSystem.handlers.handlerUser as handlerUser

import addons.LevelSystem.settings.settingColors as settingColors
import addons.LevelSystem.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def getTop(ctx):
    allUsersDatabase = handlerUser.getAllUsers(ctx.guild.id)

    # Sort users by level and xp
    # Level = [3] and XP = [4]
    allUsersDatabase.sort(key=lambda x: (x[3], x[4]), reverse=True)

    # Get the top 10 users
    topUsers = allUsersDatabase[:10]

    # Create the embed
    embed = discord.Embed(
        title = "Top 10",
        description = "Top 10 users of the server",
        color = settingColors.blue
    )
    
    # Add the thumbnail
    embed.set_thumbnail(url=settingThumbnail.levelIcon)

    # Add the fields
    for user in topUsers:

        # Get the user
        discordUser = ctx.guild.get_member(user[2])

        embed.add_field(
            name = discordUser.name,
            value = f"**Level** {user[3]}  **XP** {user[4]}",
            inline = False
        )

    # Send the embed
    await ctx.respond(embed=embed)