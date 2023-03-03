import addons.levelSystem.handlers.handlerUser as handlerUser

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

#Get the level and xp of a user
async def getUserLevel(ctx, user):

    # If no user is specified, the command author is used
    if user == None:
        user = ctx.author

    # Get the user data
    userData = handlerUser.getUser(ctx.guild.id, user.id)[0]

    # Extract the data
    userLevel = userData[3]
    userXP = userData[4]

    # Calculate the next level
    nextLevel = userLevel * 100

    # Create the embed
    embed = discord.Embed(title="Level "+ user.name, color=green)
    embed.add_field(name="Level", value=f"```{userLevel}```", inline=True)
    embed.add_field(name="XP", value=f"```{userXP}/{nextLevel}```", inline=True)
    embed.set_thumbnail(url=user.display_avatar)

    # Create the progress bar
    progress = int(userXP / nextLevel * 10)
    progressBar = "🟩" * progress + "⬜" * (10 - progress)
    embed.add_field(name="Progression", value=f"{progressBar}", inline=False)

    # Send the embed
    await ctx.respond(embed=embed)