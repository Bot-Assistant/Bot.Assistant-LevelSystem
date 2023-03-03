import addons.LevelSystem.handlers.handlerReward as handlerReward

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

# Create a reward
async def createReward(ctx, level, role, actionType):

    # Convert the action type to an integer
    if actionType == "Add role":
        actionType = 1
    elif actionType == "Remove role":
        actionType = 2

    # Create the reward in the database
    handlerReward.addReward(ctx.guild.id, level, role.id, actionType)

    # Create the embed
    embed = discord.Embed(title="Reward created", color=green)
    embed.add_field(name="Level", value=f"```{level}```", inline=True)
    embed.add_field(name="Role", value=f"```{role.name}```", inline=True)
    embed.add_field(name="Action", value=f"```{actionType}```", inline=True)

    # Send the embed
    await ctx.respond(embed=embed)